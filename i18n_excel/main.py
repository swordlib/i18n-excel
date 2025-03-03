#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from i18n_excel.json_to_excel import json_to_excel
from i18n_excel.excel_to_json import excel_to_json

def main():
    """i18n Excel 转换工具的主入口点"""
    
    # 创建主解析器
    parser = argparse.ArgumentParser(
        description='i18n Excel 转换工具 - 在Excel和JSON格式之间转换多语言翻译文件',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # JSON到Excel转换
  i18n-excel json2excel ./testdata --output translations.xlsx
  
  # Excel到JSON转换（单语言）
  i18n-excel excel2json ./output translations.xlsx zh-CN
  
  # Excel到JSON转换（多语言）
  i18n-excel excel2json ./output translations.xlsx "zh-CN,en-US,zh-TW"
        '''
    )
    
    # 创建子命令解析器
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # JSON到Excel转换子命令
    json2excel_parser = subparsers.add_parser(
        'json2excel', 
        help='将i18n JSON文件转换为Excel'
    )
    json2excel_parser.add_argument(
        'input_dir', 
        help='包含i18n JSON文件的目录'
    )
    json2excel_parser.add_argument(
        '--output', '-o', 
        default='i18n_translations.xlsx', 
        help='输出的Excel文件名（默认: i18n_translations.xlsx）'
    )
    
    # Excel到JSON转换子命令
    excel2json_parser = subparsers.add_parser(
        'excel2json', 
        help='将Excel文件转换为i18n JSON文件'
    )
    excel2json_parser.add_argument(
        'output_dir', 
        help='JSON文件的输出目录'
    )
    excel2json_parser.add_argument(
        'excel_file', 
        help='输入的Excel文件路径'
    )
    excel2json_parser.add_argument(
        'language', 
        help='要生成的语言代码，多个语言用逗号分隔（例如: "zh-CN,en-US,zh-TW"）'
    )
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 如果没有指定命令，显示帮助信息
    if not args.command:
        parser.print_help()
        return
    
    # 根据子命令执行相应的功能
    if args.command == 'json2excel':
        json_to_excel(args.input_dir, args.output)
    elif args.command == 'excel2json':
        excel_to_json(args.output_dir, args.excel_file, args.language)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1) 