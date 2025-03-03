# i18n Excel 转换工具

这是一个用于i18n国际化项目的工具集，可以在Excel格式和JSON格式之间转换多语言翻译文件。

## 功能

- **JSON到Excel转换**: 将多个语言的i18n JSON文件合并到一个Excel文件中
- **Excel到JSON转换**: 将Excel文件中的翻译内容转换回多个语言的JSON文件

## 依赖项

在使用这些工具前，需要安装以下Python库：

```bash
pip install pandas openpyxl
```

## 使用说明

### 使用统一命令行界面 (推荐)

该工具提供了统一的命令行界面，可以通过 `main.py` 访问所有功能：

```bash
# 查看帮助信息
python main.py --help

# JSON到Excel转换
python main.py json2excel <i18n文件目录> [--output <输出的Excel文件>]

# Excel到JSON转换
python main.py excel2json <输出目录> <Excel文件路径> <语言代码>
```

示例：
```bash
# JSON到Excel转换
python main.py json2excel ./testdata --output translations.xlsx

# Excel到JSON转换（单语言）
python main.py excel2json ./output translations.xlsx zh-CN

# Excel到JSON转换（多语言）
python main.py excel2json ./output translations.xlsx "zh-CN,en-US,zh-TW"
```

### 使用单独的脚本

也可以直接使用单独的脚本：

#### JSON到Excel转换

将包含多种语言JSON文件的目录转换为单个Excel文件。

```bash
python json-to-excel.py <i18n文件目录> [--output <输出的Excel文件>]
```

参数说明：
- `<i18n文件目录>`: 包含多个语言JSON文件的目录
- `--output <输出的Excel文件>`: 可选，指定输出的Excel文件名，默认为`i18n_translations.xlsx`

例如：
```bash
python json-to-excel.py ./testdata --output translations.xlsx
```

#### Excel到JSON转换

将Excel文件转换回一个或多个语言的JSON文件。

```bash
python excel-to-json.py <输出目录> <Excel文件路径> <语言代码>
```

参数说明：
- `<输出目录>`: JSON文件的输出目录
- `<Excel文件路径>`: 输入的Excel文件路径
- `<语言代码>`: 要生成的语言代码，多个语言用逗号分隔

例如：
```bash
# 生成单个语言的JSON文件
python excel-to-json.py ./output translations.xlsx zh-CN

# 生成多个语言的JSON文件
python excel-to-json.py ./output translations.xlsx "zh-CN,en-US,zh-TW"
```

## 文件格式说明

### JSON文件格式

每个语言对应一个JSON文件（例如：`zh-CN.json`，`en-US.json`），文件内容是嵌套的JSON对象，例如：

```json
{
  "module1": {
    "Hello": "你好"
  },
  "module2": {
    "Hello": "你好",
    "subModule": {
      "subHello": "子模块你好"
    }
  }
}
```

### Excel文件格式

生成的Excel文件包含以下列：

1. 每种语言对应一列（例如：`zh-CN`，`en-US`，`zh-TW`）
2. `module`列：表示JSON中的第一层key
3. `key`列：表示JSON中从第二层开始的键路径，用点号(.)连接

例如：
| zh-CN | en-US | module | key |
|-------|-------|--------|-----|
| 你好 | Hello | module1 | Hello |
| 你好 | Hello | module2 | Hello |
| 子模块你好 | Submodule Hello | module2 | subModule.subHello |

## 示例数据

项目中的`testdata`目录包含了示例JSON文件，可以用来测试这些转换工具。 