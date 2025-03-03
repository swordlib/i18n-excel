#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import pandas as pd
from collections import defaultdict

def flatten_json(json_data, module, prefix="", flattened=None):
    """将嵌套的JSON数据扁平化，使用点(.)连接键"""
    if flattened is None:
        flattened = {}
    
    for key, value in json_data.items():
        new_key = f"{prefix}.{key}" if prefix else key
        
        if isinstance(value, dict):
            flatten_json(value, module, new_key, flattened)
        else:
            flattened[(module, new_key)] = value
            
    return flattened

def json_to_excel(input_dir, output_file="i18n_translations.xlsx"):
    """
    将i18n JSON文件转换为Excel
    
    参数:
    input_dir -- 包含i18n JSON文件的目录
    output_file -- 输出的Excel文件名
    """
    # 存储所有扁平化的翻译
    all_translations = {}
    languages = []
    
    # 遍历目录中的所有JSON文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            # 提取语言代码 (文件名)
            language = os.path.splitext(filename)[0]
            languages.append(language)
            
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    json_data = json.load(f)
                    # 对每个模块扁平化JSON
                    flattened_data = {}
                    for module, module_data in json_data.items():
                        module_flattened = flatten_json(module_data, module)
                        flattened_data.update(module_flattened)
                    
                    all_translations[language] = flattened_data
                except json.JSONDecodeError:
                    print(f"无法解析JSON文件: {file_path}")
    
    if not languages:
        print("没有找到JSON文件")
        return
    
    # 创建一个包含所有键的集合
    all_keys = set()
    for lang_data in all_translations.values():
        all_keys.update(lang_data.keys())
    
    # 准备DataFrame数据
    df_data = []
    for key in sorted(all_keys):
        module, translation_key = key
        row = {
            'module': module,
            'key': translation_key
        }
        
        # 添加每种语言的翻译
        for lang in languages:
            row[lang] = all_translations[lang].get(key, '')
        
        df_data.append(row)
    
    # 创建DataFrame
    df = pd.DataFrame(df_data)
    
    # 重新排列列，使语言列在前面
    columns = languages + ['module', 'key']
    df = df[columns]
    
    # 保存到Excel
    df.to_excel(output_file, index=False)
    print(f"已将i18n数据保存到: {output_file}") 