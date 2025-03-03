# i18n Excel 转换工具

这是一个用于i18n国际化项目的工具集，可以在Excel格式和JSON格式之间转换多语言翻译文件。

## 功能

- **JSON到Excel转换**: 将多个语言的i18n JSON文件合并到一个Excel文件中
- **Excel到JSON转换**: 将Excel文件中的翻译内容转换回多个语言的JSON文件
  - 支持按键排序，输出有序的JSON文件，便于版本控制
  - 支持一次性生成多种语言的JSON文件

## 安装

### 依赖项

在使用这些工具前，需要安装以下Python库：

```bash
pip install pandas openpyxl
```

### 安装为系统命令

可以将i18n-excel工具安装为系统命令，这样可以在任何目录下直接使用：

```bash
# 开发模式安装（源码目录中的修改会直接生效）
pip install -e .

# 或者正式安装
pip install .
```

## 使用说明

安装后，可以在任何目录下使用`i18n-excel`命令：

```bash
# 查看帮助信息
i18n-excel --help

# JSON到Excel转换
i18n-excel json2excel <i18n文件目录> [--output <输出的Excel文件>]

# Excel到JSON转换
i18n-excel excel2json <输出目录> <Excel文件路径> <语言代码>
```

### 使用示例

```bash
# JSON到Excel转换
i18n-excel json2excel ./testdata --output translations.xlsx

# Excel到JSON转换（单语言）
i18n-excel excel2json ./output translations.xlsx zh-CN

# Excel到JSON转换（多语言）
i18n-excel excel2json ./output translations.xlsx "zh-CN,en-US,zh-TW"
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