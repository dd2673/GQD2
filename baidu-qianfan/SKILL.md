---
name: baidu-qianfan
description: 百度千帆API工具集，提供智能搜索、百度搜索、百度百科、百科词条、秒懂百科、热榜查询、视频AI笔记、商品营销文案、PPT生成、相似图搜索、学术检索等多种AI能力。当用户需要进行网络搜索、百科查询、热榜查看、内容生成、学术检索时自动激活。
argument-hint: [功能] [查询内容]
user-invocable: true
disable-model-invocation: false
---

# 百度千帆API技能

提供百度千帆平台的多种AI能力，包括搜索、百科、内容生成等功能。

## API配置

- **API Key**: `YOUR_API_KEY_HERE`
- **速率限制**: 3 QPS

## 可用功能

### 搜索类

| 功能 | 每日配额 | 说明 |
|------|---------|------|
| 智能搜索生成 | 100次 | AI增强的智能搜索 |
| 百度搜索 | 1000次 | 百度搜索引擎 |
| 高性能版智能搜索生成 | 100次 | 高性能智能搜索 |
| 百度学术检索 | 1000次 | 学术论文检索 |

### 百科类

| 功能 | 每日配额 | 说明 |
|------|---------|------|
| 百度百科 | 1000次 | 百科词条查询 |
| 百科词条 | 100次 | 词条详情获取 |
| 秒懂百科 | 100次 | 视频百科 |
| 百科星图列表查询 | 100次 | 星图数据查询 |

### 热榜类

| 功能 | 每日配额 | 说明 |
|------|---------|------|
| 垂类热榜查询 | 10次 | 分类热榜 |
| 热榜榜单查询 | 10次 | 热门榜单 |

### 内容生成类

| 功能 | 每日配额 | 说明 |
|------|---------|------|
| 视频AI笔记 | 10800秒 | 视频内容提取 |
| 智能商品营销文案生成 | 10次 | 商品文案 |
| 商品生动化标题生成 | 10次 | 商品标题 |
| 指令智能生成PPT | 5次 | 指令式PPT |
| 智能生成PPT | 50次 | 智能PPT |

### 其他

| 功能 | 每日配额 | 说明 |
|------|---------|------|
| 相似图搜索 | 100次 | 图片相似搜索 |

## 使用方式

调用脚本执行API请求：

```python
python ~/.iflow/skills/baidu-qianfan/scripts/qianfan.py <功能名> <参数>
```

### 示例

1. **智能搜索**：
   ```
   python qianfan.py smart_search "人工智能发展趋势"
   ```

2. **百度百科查询**：
   ```
   python qianfan.py baike "量子计算"
   ```

3. **热榜查询**：
   ```
   python qianfan.py hot_list "科技"
   ```

4. **学术检索**：
   ```
   python qianfan.py academic "大语言模型"
   ```

5. **商品文案生成**：
   ```
   python qianfan.py product_copy "智能手表，健康监测，运动追踪"
   ```

## API文档链接

- [智能搜索生成](https://cloud.baidu.com/doc/qianfan-api/s/Hmbu8m06u)
- [百度搜索](https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5)
- [百度百科](https://cloud.baidu.com/doc/qianfan/s/bmh4stpbh)
- [百科词条](https://cloud.baidu.com/doc/qianfan/s/Zmh4stpel)
- [秒懂百科](https://cloud.baidu.com/doc/qianfan/s/Mmh4stp99)
- [垂类热榜查询](https://cloud.baidu.com/doc/qianfan/s/Lmhcvvxb2)
- [热榜榜单查询](https://cloud.baidu.com/doc/qianfan/s/Amhcvzqs0)
- [视频AI笔记](https://cloud.baidu.com/doc/qianfan/s/qmhcvrqt4)
- [智能商品营销文案生成](https://cloud.baidu.com/doc/qianfan/s/Emhcw56e1)
- [商品生动化标题生成](https://cloud.baidu.com/doc/qianfan/s/9mhcw5u3y)
- [指令智能生成PPT](https://cloud.baidu.com/doc/qianfan/s/Mmhcvtke6)
- [相似图搜索](https://cloud.baidu.com/doc/qianfan/s/Pmir40a3x)
- [百科星图列表查询](https://cloud.baidu.com/doc/qianfan/s/cmi721sy9)
- [高性能版智能搜索生成](https://cloud.baidu.com/doc/qianfan/s/Kmiy99ziv)
- [智能生成PPT](https://cloud.baidu.com/doc/qianfan/s/4mjcnolh6)
- [百度学术检索](https://cloud.baidu.com/doc/qianfan/s/Amkw9qpzd)

## 注意事项

1. 注意每日配额限制，合理使用
2. 速率限制为3 QPS，避免频繁请求
3. 部分功能可能需要额外参数，请参考API文档
