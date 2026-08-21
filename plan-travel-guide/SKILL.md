---
name: plan-travel-guide
description: Use when planning destination/date-based travel guides that need current social-platform, map, OTA, ticketing, and local web discovery for dense POI tables, TopK choices, travel themes, restaurants, cafes, shops, attractions, shows, activities, exhibitions, scene/photo spots, and day-by-day routes.
---

# Plan Travel Guide

## Overview

Build a travel guide from user inputs by first learning what the requested themes mean in the destination from current public platform results, while also sweeping map, OTA, ticketing, mall-directory, and local-business categories so low-social-signal but highly relevant activity venues are not missed. Use that combined evidence to discover, verify, rank, and route POIs.

Core principle: social posts are discovery signals, not final facts, and social virality is not the whole POI universe. Platform results define the theme vocabulary and candidate content for this trip; maps, official pages, business profiles, OTA pages, ticketing pages, mall directories, booking pages, and other public sources discover and verify time-sensitive facts.

Do not maintain a fixed theme-to-POI taxonomy or keep adding one-off examples after misses. Misses should improve the theme discovery process, not create permanent special cases.

## Inputs

Require at minimum:

- Destination

Dates are strongly preferred for multi-day trips, ticketed attractions, shows, exhibitions, seasonal routes, and events. If dates are missing for a local, evergreen, neighborhood, commercial-district, or half-day planning request, do not pause by default: use the current date or near-term public status for verification, label date-sensitive facts as `需当日确认`, and avoid scheduling uncertain session-based POIs as hard anchors.

Use reasonable defaults instead of pausing when optional inputs are missing:

| Optional input | Default if missing |
|---|---|
| Lodging location | Choose a central transit-friendly area after research |
| Traveler count | 1-2 adults |
| Elders or children | None |
| Budget | Mid-range |
| Interests | Balanced: attractions, local food, cafes, shops, neighborhoods |
| Travel themes | Balanced: 本地特色, 烟火气, 拍照出片 |
| Driving | No self-driving; prefer walking, transit, taxis, rideshare |
| Daily pace | Moderate |
| Activity mode | If the user asks for `活动`, `有趣的店`, `商圈`, `一下午`, `约会`, `年轻人`, `室内`, or `多逛逛`, include experiential POIs by default: shows, immersive theater, exhibitions, pet cafes, sports/arcade/VR, workshops, board games, escape rooms, pop-ups, and mall entertainment |
| Missing dates | For half-day/local evergreen routes, use current or near-term status and flag `需当日确认`; for event-led or reservation-led trips, ask for dates before final routing |

Ask a follow-up only when destination is missing, when exact dates are essential to feasibility, or when a user-provided constraint changes feasibility materially.

## Research Workflow

1. Parse constraints: destination, dates, trip length, lodging, group needs, budget, interests, travel themes, mobility, driving mode, and pace.
2. Run **Map/OTA/Ticketing Category Sweep / 地图票务候选池扫描** before or in parallel with social theme discovery, especially for focused neighborhoods, malls, commercial districts, half-day routes, date routes, rainy-day routes, and any request containing `活动`, `有趣`, `店`, `逛`, `玩`, `剧场`, `展`, `宠物`, `运动`, or `室内`:
   - Sweep at least two non-social source families when available: Trip.com/Ctrip, Dianping, Amap, Baidu Maps, Tencent Maps, official mall directories, official scenic/venue pages, Maoyan, Damai, Douban Events, ticketing mini-site snippets, local tourism boards, and local media.
   - Search category queries, not only named POI queries. Include `周边玩乐`, `休闲娱乐`, `演出`, `脱口秀`, `即兴喜剧`, `沉浸式`, `互动剧`, `实景演绎`, `剧本杀`, `密室`, `VR`, `电玩`, `桌游`, `宠物咖`, `猫咖`, `狗咖`, `猪咖`, `蹦床`, `运动城`, `攀岩`, `保龄球`, `展览`, `展览馆`, `快闪`, `手作`, `DIY`, `市集`, `电影院`, `KTV`, and destination/neighborhood aliases.
   - For mall-heavy routes, search by mall and floor/wing aliases, such as `A馆`, `B馆`, `C馆`, `D馆`, `E馆`, `连廊`, `负一层`, `6楼`, `新玛特`, `吾悦`, `恒隆`, `大悦城`, and nearby metro exits.
   - Record named venues and product pages even when they have weak social buzz. An OTA/map listing with ticketing, hours, floor, price, or reviews can be a strong candidate for activity planning.
   - Keep suspended, closed, or schedule-dependent venues in the candidate pool only as `低置信/需确认备选`, and do not schedule them as anchors until open status, dates, and session times are verified.
3. Run **Theme Reconnaissance / 平台先导主题发现** before final POI selection:
   - For each selected theme, search the destination, neighborhood, nearby transit corridor, and lodging area across public results from 小红书/Rednote, 抖音, 微博/新浪, B站, general web search, local media, and blogs.
   - The first pass asks `这个主题在这里通常被怎么玩/怎么说/怎么拍/怎么逛`, not `有哪些固定 POI`.
   - Read accessible posts, search-result snippets, titles, captions, hashtags, comments exposed in search, and list pages. If a platform cannot be opened, use search snippets and corroborating public sources, and mark the evidence as limited.
   - Target at least two platform families when available. If evidence is thin, broaden from hotel block -> neighborhood -> district -> city, then label the theme coverage as weak if it remains thin.
4. Build a private **Theme Profile / 主题画像** for each selected theme:
   - Theme vocabulary: recurring words, hashtags, slang, fandom terms, style labels, route labels, and negative/avoidance terms.
   - Content categories: explicit venues, shops, restaurants, exhibitions, shows, activity venues, pet cafes, sports/arcade venues, workshops, events, scene/photo spots, filming or pilgrimage locations, street textures, behaviors, time windows, and crowd/booking patterns.
   - Entities to expand: names of stores, streets, buildings, artists, brands, works, characters, teams, events, dishes, products, or landmarks surfaced by the platform results.
   - Geography hints: clusters, MTR exits, mall floors, street numbers, walkable corridors, and places repeatedly paired in posts.
   - Evidence strength: high/medium/low based on repetition, specificity, source diversity, and freshness.
5. Maintain a **Discovery Evidence Matrix / 发现证据矩阵** while researching:

   | Theme | Platform/source | Query or source cue | Observed vocabulary/categories | Candidate entities | Evidence strength |
   |---|---|---|---|---|---|

   This matrix is working evidence. Do not output it as a third top-level section, but use it to populate `主题证据/来源平台` in the POI table. It must include social platforms and non-social category sources when the route is neighborhood-, mall-, activity-, or half-day-focused.
6. Generate the second-pass POI search matrix from the Theme Profile and category sweep, not from a static theme table:
   - Explicit POI queries: named venues, stores, restaurants, exhibitions, shows, theaters, sports venues, pet cafes, workshops, markets, and events surfaced by platform, map, OTA, mall-directory, or ticketing evidence.
   - Scene and behavior queries: photo spots, pilgrimage, same-angle shots, filming locations, streetscapes, buildings, bridges, stairs, waterfronts, night routes, browsing routes, show routes, pet-cafe routes, game routes, sport routes, craft routes, or other behaviors found in the profile.
   - Alias queries: simplified/traditional Chinese, English names, romanizations, old names, common typos, fan nicknames, mall/floor/shop numbers, nearby exits, and nearby landmarks when the profile suggests alias risk.
   - Verification queries: address, open/closed status, hours, ticketing, booking, session times, show calendars, age/height/health restrictions, pet interaction rules, menu/product availability, temporary pop-ups, construction, and closure risks.
7. Read source content deeply enough to extract concrete evidence:
   - Named dishes, products, shop floors, show times, ticket types, prices, experience duration, rules, visual features, queue advice, booking notes, route pairings, exact camera positions, time-of-day advice, or why the place fits the theme.
   - When only generic praise exists, keep the POI lower-ranked or label it low confidence.
8. Build a candidate pool before choosing the itinerary:
   - For a focused one-day neighborhood plan, target 20-40 candidate POIs before pruning.
   - For a focused half-day commercial-district plan, target 15-30 candidate POIs before pruning, including at least 5-10 activity or experience POIs when source coverage exists.
   - For multi-day city plans, target at least 10-15 candidate POIs per day or 30-60 total.
   - Keep at least 70% of POIs as concrete named venues, stores, activity venues, scenes, or route points, not generic streets, malls, or districts.
   - For `有趣的店/活动/半日/商圈` requests, do not let restaurants, generic mall anchors, or social-media-famous photo spots crowd out experiential POIs. Include TopK coverage for at least three of: shows, immersive theater, exhibitions, pet cafes, sports/arcade/VR, workshops, board games/escape rooms, bookstores/culture, and pop-ups. If fewer than three exist, say evidence is thin.
9. Deduplicate aliases and branches. Merge Chinese/English names, simplified/traditional forms, common typos, nicknames, branch names, mall names, floor names, product names, ticket-page names, and same-place variants. Keep branch names when location matters.
10. Verify time-sensitive facts with reliable public sources:
   - Address or area
   - Open/closed status
   - Opening hours and closed days
   - Reservation, ticket, queue requirement, session/show time, last entry, activity duration, refund/cancellation constraints
   - Restrictions such as age, height, physical intensity, pregnancy/heart-condition warnings, pet allergies, animal welfare/sanitation concerns, dress code, and photo/video rules
   - Seasonal limits, temporary event dates, construction, weather sensitivity, last-entry rules
11. Rank POIs by combined signal:
   - Platform repetition and enthusiasm, especially Xiaohongshu when available
   - Source diversity across social platforms, maps, OTA pages, ticketing pages, official pages, mall directories, and public web
   - Specificity of evidence, such as named dish, product, floor, show/session time, ticket type, activity duration, exact scene, camera angle, queue tip, or route pairing
   - Fit with the Theme Profile, user interests, group constraints, budget, pace, and dates
   - Current feasibility and geographic fit
12. Cluster POIs by geography and route logic. Prefer same-area days and avoid needless backtracking.
13. Build a realistic itinerary with meals near route clusters, travel time considered, and backup options for weather, closures, crowds, sold-out sessions, fatigue, weak theme coverage, allergies, or physical-intensity mismatch.

## Theme Handling

Themes are labels to investigate, not predefined POI categories. Use seed terms only to start the first few searches; replace them with the live Theme Profile once platform evidence appears.

Seed prompts for common themes:

| Theme | Initial probes only |
|---|---|
| 情侣约会 | 约会, 氛围感, 夜景, 散步, 甜品, 酒吧, 安静, 浪漫 |
| 二次元 | 动漫, 谷子, 手办, 模型, IP展, 联名, 圣地巡礼, 同款机位, 角色, 作品 |
| 复古文艺探店 | 复古, 文艺, 独立咖啡, 旧书, 唱片, 胶片, 古着, 老建筑 |
| 运动文化 | 球鞋, 球衣, 街头, skate, running, basketball, 赛事, 球场 |
| 体验活动 | 周边玩乐, 休闲娱乐, 演出, 剧场, 脱口秀, 即兴喜剧, 沉浸式, 互动剧, 实景演绎, 剧本杀, 密室, VR, 电玩, 桌游, 宠物咖, 猫咖, 狗咖, 猪咖, 蹦床, 运动城, 攀岩, 展览, 手作, DIY, 快闪 |
| 传统文化 | 寺庙, 博物馆, 老街, 历史, 非遗, 手作, 茶, 庙会 |
| 本地特色 | 老字号, 茶餐厅, 冰室, 点心, 烧味, 云吞面, 煲仔饭 |
| 烟火气 | 街市, 夜市, 大排档, 小吃, 排队, 本地人, 平价 |
| 拍照出片 | 机位, 打卡, 出片, 霓虹, 天桥, 海滨, 街景, 建筑 |
| 自然风光 | 公园, 海滨, 山径, 郊游, 日落, 海景, 花期, 观景 |

Theme rules:

- If the user gives multiple themes, build the route around the strongest 1-2 Theme Profiles and use the rest as secondary filters. Do not average all themes into a generic route.
- If platform results show an unexpected interpretation of a theme, follow the evidence. For example, a theme may become a route, scene type, event, food style, shopping behavior, or fandom practice rather than a store category.
- If the user's language is broad (`有趣`, `活动`, `多逛逛`, `一下午`, `约会`, `年轻人`, `商圈`), treat it as a mixed theme, not only shopping. Build parallel profiles for `逛店/消费`, `体验活动`, and `吃喝休息`, then rank by time fit and current availability.
- If the Theme Profile is weak, say `主题覆盖较弱`, show the best-supported alternatives, and avoid overclaiming.
- Do not claim an IP, film, anime, game, MV, historical story, or celebrity association as canonical unless a source explicitly supports it. If evidence supports only visual similarity or fan practice, label it as `场景感/粉丝打卡`.
- For temporary events, exhibitions, pop-ups, collaborations, and seasonal spots, verify the exact dates before recommending them for the itinerary.
- For shows, immersive experiences, sports venues, pet cafes, workshops, and ticketed exhibitions, verify session times and activity status before scheduling. If verification is conflicting, include as `需确认备选` rather than a route anchor.

## TopK and Style Coverage

Do not collapse a neighborhood into one generic recommendation. Provide ranked choices for each important decision slot.

For meals, include TopK options across styles when available:

| Dining style | Examples of what to search for |
|---|---|
| 本地特色 | 茶餐厅、冰室、烧味、点心、煲仔饭、云吞面、大排档 |
| 平价高分 | 米其林必比登、OpenRice 高分、排队老店、性价比 |
| 甜品小吃 | 鸡蛋仔、糖水、蛋挞、菠萝油、街头小吃 |
| 咖啡/Brunch | 独立咖啡、设计感咖啡、早午餐、烘焙 |
| 异国/换口味 | 日式、韩式、泰式、越南、意大利、素食、清真 |
| 夜宵/夜生活 | 夜市、居酒屋、酒吧、深夜甜品、宵夜档 |

For activities, include TopK options across formats when available:

| Activity style | Examples of what to search for |
|---|---|
| 演出/喜剧 | 剧场、脱口秀、即兴喜剧、魔术、二人转、小剧场、开放麦、演出排期 |
| 沉浸体验 | 沉浸式互动剧、实景演绎、城市逃脱、剧本杀、密室、NPC互动、角色扮演 |
| 展览/文化 | 临时展、主题展、商场展、博物馆、艺术空间、历史展馆、快闪展 |
| 宠物互动 | 猫咖、狗咖、猪咖、柴犬咖、哈士奇咖、宠物桌游、动物互动规则 |
| 运动娱乐 | 蹦床、运动城、攀岩、跑酷、镭射CS、保龄球、旱雪、电玩、VR |
| 手作/轻社交 | DIY、手工、陶艺、香薰、银饰、拼豆、桌游、手账、书店活动 |

For shopping, scenes, and wandering, derive categories from the Theme Profile first, then fill general coverage:

| Coverage type | What to include when supported |
|---|---|
| 主题显性点 | Stores, exhibitions, events, restaurants, venues directly surfaced by platform evidence |
| 场景/巡礼/机位 | Buildings, bridges, stairs, streetscapes, filming or fan-recognized spots, exact photo angles |
| 主题行为线 | Browsing, collecting, cafe hopping, citywalk, night photos, craft experience, sport route, local market route |
| 街头市集 | Night markets, wet markets, flower streets, flea/old-goods areas |
| 设计文创/中古 | Bookstores, stationery, gallery shops, vinyl, camera, vintage, toy/model shops |
| 商场精选 | Concrete stores or sub-stops inside malls, not only mall names |
| 体验活动 | Named shows, pet cafes, sport/arcade venues, exhibitions, workshops, immersive experiences, ticketed events, not only the mall name |

Guidance:

- For each meal slot, choose one primary recommendation and include 2-4 alternatives with different styles.
- For a shopping/street-walk segment, list named stores, scenes, or sub-stops where possible. A mall or street can be an anchor, but it should not replace concrete child POIs.
- For a mall or commercial-district segment, list both retail stores and activity venues. Do not let social-media-famous shops crowd out quieter but itinerary-useful ticketed or map-listed venues.
- If the user specifies themes, rank TopK inside the strongest Theme Profiles before general style buckets.
- If a category has weak evidence, keep it only when it expands useful style coverage and label it `低置信备选`.

## Source Handling

- Cite Xiaohongshu source links when available. If search results expose only snippets, say `搜索结果摘要` and include the result URL when possible.
- Use 抖音, 微博/新浪, B站, local media, blogs, OpenRice, Trip.com/Ctrip, Dianping, Amap, Baidu Maps, Tencent Maps, Maoyan, Damai, Douban Events, Time Out, tourism-board pages, mall directories, official sites, map/business profiles, and booking pages as appropriate for discovery or verification.
- For platform-derived POIs, record what the source actually supports: repeated mentions, exact shop/product, dish, visual style, queue warning, route pairing, scene, camera angle, event date, or weak mention.
- For OTA/map/ticketing-derived POIs, record what the source actually supports: address, floor, hours, ticket price, package, show/session time, activity duration, open/suspended status, reviews, age/height restrictions, and booking notes.
- Use current web verification for facts likely to change: hours, closure, ticketing, show calendars, activity sessions, shop status, menu availability, prices, transport schedules, exhibitions, events, and regulations.
- If sources conflict, state the uncertainty in `注意事项` and choose the safer itinerary option.
- Do not fabricate source links, pretend blocked posts were read, or present an unverified business as open.

## POI Table

Always output this as section `1）完整 POI 总表`.

Use one row per deduplicated POI. Keep all required fields and include theme evidence:

| 名称 | 类型 | 风格/主题定位 | 区域 | 推荐理由 | 主题证据/来源平台 | 小红书出现频率/推荐度 | TopK/排序 | 建议停留时间 | 注意事项 | 来源帖子链接 |
|---|---|---|---|---|---|---|---|---|---|---|

Guidance:

- `名称`: prefer concrete named venues, stores, scenes, route points, and event names. Use generic streets, malls, or districts only as route anchors, and list representative child POIs separately.
- `类型`: 景点 / 餐厅 / 小吃 / 咖啡 / 商店 / 市集 / 展览 / 演出 / 剧场 / 沉浸体验 / 宠物咖 / 运动娱乐 / 手作 / 桌游密室 / 夜生活 / 街区 / 周边游 / 机位 / 巡礼 / 取景地 / 活动 / 其他.
- `风格/主题定位`: be specific and evidence-derived, such as `二次元/平台归纳-巡礼机位`, `复古文艺/旧书咖啡`, `烟火气/夜市小吃`, `本地特色/老派冰室`, `拍照出片/霓虹街景`, or `低置信备选`.
- `推荐理由`: include concrete evidence or use case. Avoid generic copy like `很有特色` unless supported by a named dish, product, ticketed activity, show format, floor, duration, view, design feature, platform pattern, or source note.
- `主题证据/来源平台`: summarize why this POI fits the Theme Profile, naming platforms or source types, e.g. `小红书+抖音多次出现为夜景机位`, `微博/本地媒体提到临时展`, `OpenRice 验证餐厅状态`.
- `小红书出现频率/推荐度`: use `高 / 中 / 低 / 未见明确小红书证据` plus brief evidence. Other platform strength belongs in `主题证据/来源平台`.
- `TopK/排序`: rank within a style or theme bucket, e.g. `主题-巡礼 Top1`, `本地午餐 Top2`, `咖啡 Top3`, `购物-文创 Top1`, `夜宵备选`.
- `建议停留时间`: be concrete, e.g. `20-30 分钟`, `30-45 分钟`, `1.5-2 小时`, `半天`.
- `注意事项`: include reservations, closed days, queues, weather, ticketing, show/session times, last entry, age/height/health restrictions, pet allergies, child/elder suitability, best time, evidence limits, or uncertainty.

## Itinerary

Always output this as section `2）按天行程`.

For each day, use this fixed structure:

```markdown
### Day N：区域主题

| 时段 | 安排 | 建议停留时间 | 移动顺序/交通 | 备注 |
|---|---|---|---|---|
| 上午 |  |  |  |  |
| 午餐 |  |  |  |  |
| 下午 |  |  |  |  |
| 晚餐 |  |  |  |  |
| 晚上 |  |  |  |  |

TopK 备选：
- 主题路线：主线 ...；主题替换线 ...
- 早餐/早午餐：Top1 ...；Top2 ...；Top3 ...
- 午餐：Top1 ...；Top2 ...；Top3 ...
- 咖啡/甜品：Top1 ...；Top2 ...；Top3 ...
- 购物/逛店：Top1 ...；Top2 ...；Top3 ...
- 活动/体验：Top1 ...；Top2 ...；Top3 ...
- 演出/展览：Top1 ...；Top2 ...；Top3 ...
- 场景/巡礼/机位：Top1 ...；Top2 ...；Top3 ...
- 晚餐/夜宵：Top1 ...；Top2 ...；Top3 ...
```

Itinerary rules:

- Cluster each day around one main area or route corridor unless the user asks for a high-intensity trip.
- Put hard-time items first: ticketed entries, exhibitions, show/session times, immersive theater slots, sports-venue booking windows, pet-cafe appointments, sunsets, performances, restaurant reservations, market hours, and temporary pop-ups.
- Balance anchor POIs with nearby meals, cafes, shops, scenes, and short walks.
- Schedule only the best-fit POIs; leave extra POIs as TopK backups instead of overloading the day.
- For half-day commercial-district plans, schedule no more than one long activity anchor by default. Pair it with 1-2 browsing segments and 1 food/rest segment, then leave the rest as TopK backups.
- If themes are provided, name the day or route by the leading Theme Profile and include theme-specific swaps in `TopK 备选`.
- Use conservative travel time and avoid scheduling every minute.
- Adjust for arrival and departure days.
- For elders/children or relaxed pace, reduce stops and add rest blocks.
- For self-driving trips, consider parking, road conditions, scenic routes, and avoiding alcohol-centered stops before driving.
- Include backup POIs per day for bad weather, closure, full booking, crowds, fatigue, or weak theme evidence.

## Common Mistakes

- Do not start from a fixed theme table and then look for POIs that match it. Build a Theme Profile from current platform evidence first.
- Do not repair a missed POI by adding the missed case as a permanent example. Generalize the retrieval process: platform scanning, vocabulary extraction, alias expansion, evidence matrix, second-pass POI search.
- Do not stop at broad area labels such as `旺角有女人街、金鱼街、花墟`. Add concrete restaurants, cafes, shops, scenes, and style-specific alternatives.
- Do not equate `有趣的店` with only retail shops. In mall/commercial-district routes, sweep OTA/map/ticketing categories for theaters, immersive experiences, exhibitions, pet cafes, sports/arcade venues, workshops, board games, VR, and escape rooms.
- Do not rely only on social-platform virality. Map and ticketing POIs may have weak 小红书 evidence but strong route value because they provide bookable activities, floors, prices, hours, and durations.
- Do not treat one viral local restaurant as enough. Local classics can be Top1, but include non-local or different-vibe choices when the area and theme evidence support them.
- Do not ignore unexpected platform signals. If a theme is expressed through a scene, route, event, photo angle, fandom practice, or food style, include those candidates rather than forcing the theme into store categories.
- Do not put every POI into the route. The POI table is the inventory; the itinerary is the curated path.
- Do not hide uncertainty. If platforms cannot be opened, evidence is snippet-only, or facts cannot be verified, say so in the source/evidence fields.

## Final Response Checklist

Before finalizing:

- Confirm the output has exactly the two required top-level sections.
- If dates were missing, confirm assumptions, source limits, and `需当日确认` notes are embedded inside the POI table or itinerary remarks, not added as a third top-level section.
- Confirm every selected theme has a Theme Profile built from platform evidence or a clear `主题覆盖较弱` note.
- Confirm a Discovery Evidence Matrix informed POI selection, even though it is not output as a separate top-level section.
- Confirm POI searches were generated from Theme Profile categories, map/OTA/ticketing category sweeps, vocabulary, entities, aliases, scenes, and behaviors, not only from static seed terms.
- Confirm the POI table is dense enough for the request scope.
- Confirm focused neighborhood plans include concrete named venues, stores, activity venues, scenes, route points, or events, not only street or mall anchors.
- Confirm commercial-district, half-day, `有趣的店`, or `活动` requests include TopK coverage for activity/experience POIs, or explicitly explain that evidence is thin.
- Confirm selected themes appear in `风格/主题定位`, `主题证据/来源平台`, POI ranking, and TopK alternatives.
- Confirm food, cafe/dessert, shopping, activity/experience, scene/photo, and night options have TopK rankings or an explicit reason why a category is thin.
- Confirm no IP, film, anime, game, MV, historical, or celebrity claim is stated as canonical unless a source explicitly supports it.
- Confirm every scheduled POI appears in the table or as a clearly labeled backup.
- Confirm all time-sensitive facts have been checked or flagged as uncertain, including open/suspended status, show/session times, ticketing, restrictions, and last entry for activity venues.
- Confirm the route reduces backtracking by geography.
- Include source links used for discovery and verification.
