---
layout: default
title: Horizon 信息雷达
---

# Horizon 信息雷达

这是一个自动运行的信息系统：每天生成综合技术简报，每周生成 GitHub 热门项目周报和俄乌战争进展周报。

<div class="horizon-dashboard" markdown="1">

<section class="horizon-card" markdown="1">

## 每日速递

覆盖 AI/LLM 应用、AI Infra、推理/训练、AI Coding、Agent、开源趋势、产品/创业、网络安全和少量重大国际动态。

<ul class="post-list">
{% assign daily_count = 0 %}
{% for post in site.posts %}
  {% if post.lang == "zh" and post.category != "github-weekly" and post.category != "ukraine-war-weekly" %}
    {% assign daily_count = daily_count | plus: 1 %}
    {% if daily_count <= 14 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}｜{{ post.title }}</a>
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
{% if daily_count == 0 %}
  <li><em>暂无每日速递。手动运行 Daily Horizon Summary 后会出现在这里。</em></li>
{% endif %}
</ul>

</section>

<section class="horizon-card" markdown="1">

## GitHub 热门项目周报

每周整理近期 GitHub 热门项目，并用中文说明每个项目是什么、解决什么问题、大致运行原理以及为什么值得关注。

<ul class="post-list">
{% assign github_count = 0 %}
{% for post in site.posts %}
  {% if post.category == "github-weekly" %}
    {% assign github_count = github_count | plus: 1 %}
    {% if github_count <= 12 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}｜{{ post.title }}</a>
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
{% if github_count == 0 %}
  <li><em>暂无 GitHub 周报。手动运行 Weekly GitHub Trending Summary 后会出现在这里。</em></li>
{% endif %}
</ul>

</section>

<section class="horizon-card" markdown="1">

## 俄乌战争一周进展

每周汇总公开来源中的战场态势、空袭/无人机/导弹、防务援助、外交动态和不确定性提示。

<ul class="post-list">
{% assign war_count = 0 %}
{% for post in site.posts %}
  {% if post.category == "ukraine-war-weekly" %}
    {% assign war_count = war_count | plus: 1 %}
    {% if war_count <= 12 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}｜{{ post.title }}</a>
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
{% if war_count == 0 %}
  <li><em>暂无俄乌战争周报。手动运行 Weekly Russia-Ukraine War Summary 后会出现在这里。</em></li>
{% endif %}
</ul>

</section>

</div>

---

## 运行节奏

| 报告 | Workflow | 频率 | 内容 |
|---|---|---:|---|
| 每日速递 | Daily Horizon Summary | 每天 | 综合技术和趋势简报 |
| GitHub 热门项目周报 | Weekly GitHub Trending Summary | 每周一 | 热门开源项目中文解读 |
| 俄乌战争一周进展 | Weekly Russia-Ukraine War Summary | 每周一 | 最近一周公开来源态势汇总 |

## 项目

- [GitHub 仓库](https://github.com/vencentml/Horizon-vicent)
- [配置指南](configuration)
- [信息源采集器](scrapers)
- [评分系统](scoring)
