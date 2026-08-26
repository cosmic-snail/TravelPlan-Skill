# Community Sharing

## Directory Information

- **Skill Name:** Plan Travel Guide
- **Skill Source:** https://github.com/cosmic-snail/TravelPlan-Skill/tree/main/plan-travel-guide
- **Repository:** https://github.com/cosmic-snail/TravelPlan-Skill
- **Category:** Creative & Media
- **Source Platform:** GitHub
- **Tags:** Chinese-Native, Travel Planning, POI Research, Itinerary

## Install

```bash
npx skills add cosmic-snail/TravelPlan-Skill \
  --skill plan-travel-guide \
  --agent codex \
  --global
```

## Chinese Description

`plan-travel-guide` 是一个面向 Codex 的中文旅行规划 Skill。它会根据目的地、日期、同行人数、预算、交通方式和旅行主题，从社交平台、地图、OTA、票务、商场目录及公开网页中发现具体 POI，再用官网、商家页或订票页核验营业状态、日期、场次、预约与限制条件，最终输出完整 POI 总表、TopK 备选和按天行程。社交热度只作为发现信号，不会被当成营业或可订状态的证明。

## English Description

`plan-travel-guide` is a Chinese-native Codex Skill for source-led themed travel planning. It discovers concrete POIs from social platforms, maps, OTAs, ticketing sites, venue directories, and public web sources; verifies time-sensitive details with primary or reliable pages; and produces a dense POI table, TopK alternatives, and a day-by-day itinerary.

## Risk Notes

The Skill requires live web access for current POIs, opening hours, event dates, ticketing, reservations, closures, restrictions, and route feasibility. Social-platform results are discovery signals rather than proof. It does not purchase tickets, make reservations, bypass access controls, or guarantee that a venue or route remains available.

## OpenAI Developer Community Draft

**Title:** 开源 Plan Travel Guide：一个基于多来源发现与核验的 Codex 中文旅行规划 Skill

我开源了 `plan-travel-guide`，用于需要具体 POI、主题玩法和按天路线的旅行规划。它会先根据目的地收集本地词汇，再组合社交平台、地图、OTA、票务和场馆目录建立候选池，避免行程只剩网红餐厅和宽泛商圈。

对于营业时间、活动日期、票务、预约和临时闭店等时效信息，Skill 会要求使用当前公开来源交叉核验，并把证据不足的项目标为需确认。输出固定包含完整 POI 总表和按天行程，同时保留不同主题的 TopK 备选。

Repository: https://github.com/cosmic-snail/TravelPlan-Skill

Install:

```bash
npx skills add cosmic-snail/TravelPlan-Skill --skill plan-travel-guide --agent codex --global
```

欢迎反馈不同城市、平台和主题下的漏召回案例。

## English Community Draft

**Title:** Plan Travel Guide: source-led themed travel planning for Codex

I built `plan-travel-guide`, an open-source Codex Skill for travel requests that need concrete POIs, themed discovery, and executable day-by-day routes. It combines local vocabulary discovery with social platforms, maps, OTAs, ticketing sites, and venue directories so the candidate pool is not limited to viral restaurants or generic district names.

Time-sensitive details such as opening hours, event dates, tickets, reservations, closures, and restrictions must be checked against current public sources. The output includes a complete POI table, TopK alternatives, and a day-by-day itinerary, with uncertain items kept visible rather than presented as facts.

Repository: https://github.com/cosmic-snail/TravelPlan-Skill

Install:

```bash
npx skills add cosmic-snail/TravelPlan-Skill --skill plan-travel-guide --agent codex --global
```

