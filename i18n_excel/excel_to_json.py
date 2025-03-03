#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import pandas as pd
from collections import defaultdict

def nested_dict():
    """创建一个可以无限嵌套的字典"""
    return defaultdict(nested_dict)

def excel_to_json(input_dir, excel_file, language):
    """
    将Excel转换回i18n JSON文件
    
    参数:
    input_dir -- 输出的i18n文件目录
    excel_file -- 输入的Excel文件路径
    language -- 要生成的语言代码，多个语言用逗号分隔
    """
    # 确保输出目录存在
    os.makedirs(input_dir, exist_ok=True)
    
    # 读取Excel文件
    df = pd.read_excel(excel_file)
    
    # 处理多个语言（用逗号分隔）
    languages = [lang.strip() for lang in language.split(',')]
    
    for lang in languages:
        # 检查语言列是否存在
        if lang not in df.columns:
            print(f"错误: Excel文件中不存在'{lang}'列")
            continue
            
        # 创建结构化的JSON数据
        json_data = {}
        
        # 遍历每一行
        for _, row in df.iterrows():
            module = row['module']
            key_path = row['key'].split('.')
            value = row[lang]
            
            # 跳过空值
            if pd.isna(value):
                continue
                
            # 确保模块存在
            if module not in json_data:
                json_data[module] = {}
                
            # 嵌套字典以存储翻译
            current = json_data[module]
            
            # 遍历键路径（除了最后一个键）
            for key in key_path[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
                
            # 设置最后一个键的值
            current[key_path[-1]] = value
        
        # 写入JSON文件
        output_file = os.path.join(input_dir, f"{lang}.json")
        with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2, sort_keys=True)
            
        print(f"已生成 {lang} 语言的JSON文件: {output_file}") 