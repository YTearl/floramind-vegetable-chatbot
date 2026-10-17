"""
Curated Vegetable Knowledge Base
Scientifically validated agricultural guides focusing on Philippines & international standards.
Sources: DA-BPI (Bureau of Plant Industry), PCAARRD, UPLB-IPB, and FAO.
"""

VEGETABLE_DATA = [
    {
        "id": "pechay",
        "name": "Pechay (Pak Choi / Chinese Cabbage)",
        "scientific_name": "Brassica rapa subsp. chinensis",
        "family": "Brassicaceae (Mustard / Cabbage Family)",
        "local_names": ["Pechay", "Bok Choy", "Pak Choi", "Pechay Tagalog"],
        "planting_method": "Transplanting or Direct Seeding (Transplanting recommended for uniform stand)",
        "germination_period": "3–5 days (up to 7 days under cool or dry conditions)",
        "seedling_age_transplant": "10–15 days after sowing (when seedlings have 3–4 true leaves)",
        "ideal_conditions": {
            "temperature": "20°C to 30°C (can tolerate warm tropical lowland climates with partial shade)",
            "soil_type": "Well-drained sandy loam or clay loam rich in organic matter",
            "soil_ph": "5.5 to 6.8",
            "sunlight": "Full sun (minimum 6 hours daily); tolerates light afternoon shade",
            "water_needs": "Consistent, shallow watering; avoid waterlogging to prevent root rot",
            "spacing": "10–15 cm between plants, 20–25 cm between rows"
        },
        "days_to_harvest": "30–45 days from sowing (or 20–25 days after transplanting)",
        "days_to_maturity": "35–45 days depending on the variety (e.g., Black Behi reaches maturity at ~40–45 days; Pavito at ~30–35 days)",
        "harvesting_guide": "Harvest when plants reach 15–20 cm in height with 6–8 fully developed leaves before flower buds emerge. Cut the entire plant at ground level with a sharp knife early in the morning or late afternoon, or prime individual outer leaves for continuous harvest.",
        "fertilizer_recommendation": {
            "type": "Organic compost + balanced inorganic fertilizer (Complete 14-14-14) and nitrogen-rich side dress (Urea 46-0-0)",
            "nutrients": "High Nitrogen (N) for vigorous leaf growth, moderate Phosphorus (P) for seedling root establishment, and Potassium (K) for leaf crispness and disease tolerance.",
            "timing_method": "Basal: Thoroughly incorporate 5–10 tons/ha (0.5–1 kg/m²) well-decomposed compost + 10 g Complete (14-14-14) per meter row before transplanting. Side-dress: 10–14 days after transplanting, apply dissolved Urea (1 tbsp per 4 liters water or 5 g/m²) along rows.",
            "rates_summary": "100–120 kg N, 60 kg P2O5, 60 kg K2O per hectare baseline (DA-BPI guide)."
        },
        "growing_tips": "Mulch beds with rice straw or carbonized rice hull (CRH) to preserve moisture and suppress weeds. Watch for flea beetles, diamondback moth larvae, and cutworms; use neem extract or companion planting with marigold.",
        "citations": ["Bureau of Plant Industry (DA-BPI) Vegetable Production Guide - Pechay", "PCARRD Vegetable Guidebook"]
    },
    {
        "id": "ampalaya",
        "name": "Ampalaya (Bitter Gourd / Bitter Melon)",
        "scientific_name": "Momordica charantia",
        "family": "Cucurbitaceae (Gourd Family)",
        "local_names": ["Ampalaya", "Amargoso", "Bitter Gourd", "Bitter Melon"],
        "planting_method": "Direct seeding or seedling tray establishment followed by transplanting onto trellised beds",
        "germination_period": "5–9 days (scarifying or soaking seeds in warm water for 12–24 hours accelerates germination)",
        "seedling_age_transplant": "14–20 days after sowing (2 true leaf stage)",
        "ideal_conditions": {
            "temperature": "25°C to 35°C (thrives in tropical warmth and humidity)",
            "soil_type": "Deep, fertile, well-draining sandy loam with high organic humus",
            "soil_ph": "6.0 to 6.8",
            "sunlight": "Full sun (minimum 6–8 hours daily)",
            "water_needs": "Moderate to high; regular furrow or drip irrigation during flowering and fruit setting",
            "spacing": "40–50 cm between hills, 2.0–2.5 meters between trellised rows"
        },
        "days_to_harvest": "50–60 days from transplanting (or 65–75 days from direct sowing)",
        "days_to_maturity": "70–85 days to full maturity; hybrid varieties like Mestisa F1 mature earlier (~55 days after transplanting) than open-pollinated varieties (~70 days)",
        "harvesting_guide": "Harvest fruits when they are firm, deep green to light green, ribs are prominent and rounded, but before any yellowing or orange coloring begins. Harvest every 2 to 3 days using pruning shears to encourage continuous flushes of flowers and fruits for 2–3 months.",
        "fertilizer_recommendation": {
            "type": "Well-rotted animal manure / vermicompost, Complete fertilizer (14-14-14), Urea (46-0-0), and Muriate of Potash (0-0-60)",
            "nutrients": "Balanced NPK for vining, high P at root establishment, increased K during flowering and fruit elongation to prevent blossom drop.",
            "timing_method": "Basal: 10–15 g Complete (14-14-14) + 200 g compost per hill. Side-dress: At 15, 30, and 45 days after transplanting, apply 10 g Urea + 5 g Potash per hill buried 10 cm from the base.",
            "rates_summary": "120 kg N, 60 kg P2O5, 90 kg K2O per hectare (UPLB-IPB / DA-BPI Standard)."
        },
        "growing_tips": "Construct a sturdy overhead or A-frame bamboo/nylon trellis at least 1.8–2 meters high. Bag young developing fruits with perforated paper bags or netting to protect from fruit flies (Bactrocera cucurbitae).",
        "citations": ["DA-BPI Ampalaya Production Manual", "East-West Seed Cultivation Guide"]
    },
    {
        "id": "sitaw",
        "name": "Sitaw (Yardlong Bean / String Bean)",
        "scientific_name": "Vigna unguiculata subsp. sesquipedalis",
        "family": "Fabaceae (Legume / Bean Family)",
        "local_names": ["Sitaw", "Hamtak", "Yardlong Bean", "Asparagus Bean"],
        "planting_method": "Direct seeding (soaking seeds for 1–2 hours improves emergence)",
        "germination_period": "3–5 days in moist warm soil",
        "seedling_age_transplant": "Not recommended (legumes have sensitive taproots; direct seeding is standard)",
        "ideal_conditions": {
            "temperature": "22°C to 32°C (warm tropical lowland and mid-elevation)",
            "soil_type": "Friable sandy loam to clay loam; tolerates moderate soil types",
            "soil_ph": "5.5 to 6.8",
            "sunlight": "Full sunlight (minimum 6–8 hours)",
            "water_needs": "Moderate; water deeply during flowering and pod development; avoid prolonged standing water",
            "spacing": "20–30 cm between hills (2–3 seeds per hill, thinned to 2), 1 meter between rows with bamboo trellis"
        },
        "days_to_harvest": "45–55 days from sowing (climbers like Negros or Sandigan)",
        "days_to_maturity": "50–65 days depending on variety and season (bush sitaw varieties mature faster in ~45–50 days, pole varieties in ~55–65 days)",
        "harvesting_guide": "Harvest pods when they are tender, pliable, pencil-thick, and the seeds have not yet bulged visibly. Pick every 2 days by snapping or snipping the stem; harvesting regularly extends the productive lifespan up to 8–10 weeks.",
        "fertilizer_recommendation": {
            "type": "Organic compost, Starter fertilizer (16-20-0 or 14-14-14), and supplemental Muriate of Potash (0-0-60)",
            "nutrients": "Low to moderate Nitrogen (legumes fix atmospheric nitrogen via Rhizobium root nodules); high Phosphorus and Potassium for flowering and pod filling.",
            "timing_method": "Basal: 10 g Complete (14-14-14) and 100 g compost per hill at planting. Side-dress: At first flowering (around 30 days after sowing), side-dress with 5 g 14-14-14 and 3 g 0-0-60 per hill.",
            "rates_summary": "30–45 kg N, 60 kg P2O5, 60 kg K2O per hectare (excessive nitrogen causes leafy vines with poor pod set)."
        },
        "growing_tips": "Provide sturdy teepee or trellis poles (2 meters high) when vines start running at 10–14 days. Watch for aphids and pod borers (Maruca vitrata); spray soap solution or botanical neem spray before pod formation.",
        "citations": ["DA-BPI Legume Crops Production Guide", "PCAARRD Farm Bulletin"]
    },
    {
        "id": "talong",
        "name": "Talong (Eggplant / Aubergine)",
        "scientific_name": "Solanum melongena",
        "family": "Solanaceae (Nightshade Family)",
        "local_names": ["Talong", "Talong Tagalog", "Eggplant", "Brinjal"],
        "planting_method": "Seedbed or seedling tray establishment followed by transplanting to raised beds",
        "germination_period": "7–10 days (requires warm soil 24–30°C)",
        "seedling_age_transplant": "28–35 days after sowing (4–5 true leaves, sturdy stems)",
        "ideal_conditions": {
            "temperature": "22°C to 33°C (sensitive to frost and cold; loves warm sunny weather)",
            "soil_type": "Deep, fertile loam or sandy-clay loam high in organic matter",
            "soil_ph": "5.5 to 6.8",
            "sunlight": "Full sun (minimum 6–8 hours daily)",
            "water_needs": "Moderate to deep; 25–35 mm water per week; mulch heavily to preserve moisture",
            "spacing": "50–60 cm between plants, 75–100 cm between rows"
        },
        "days_to_harvest": "60–75 days from transplanting (or 90–110 days from sowing)",
        "days_to_maturity": "90–120 days total maturity; hybrid varieties like Dumaguete Long Purple, Casino 901, and Calixto F1 produce continuously for 3–6 months",
        "harvesting_guide": "Harvest when fruits reach characteristic size and develop glossy, smooth skin. Press gently with thumb: if the flesh springs back, it is ready. If it leaves a permanent dent, it is overripe and seedy. Harvest every 4–5 days using sharp shears leaving 2 cm of calyx stem.",
        "fertilizer_recommendation": {
            "type": "Decomposed manure/compost, Complete 14-14-14, Urea 46-0-0, and Muriate of Potash 0-0-60",
            "nutrients": "N for vegetative branching, high P at root stage, high K for fruit firmness and color.",
            "timing_method": "Basal: 15–20 g Complete (14-14-14) + 300 g compost per hill. Side-dress 1: At 15 days after transplanting, 5 g Urea + 5 g 14-14-14. Side-dress 2 & 3: Every 20 days during harvest, 10 g 14-14-14 per plant.",
            "rates_summary": "120–150 kg N, 60–90 kg P2O5, 90–120 kg K2O per hectare (PCAARRD / DA-BPI Standard)."
        },
        "growing_tips": "Stake plants with 1-meter bamboo stakes to prevent toppling under fruit load. Monitor for Fruit and Shoot Borer (Leucinodes orbonalis); prune infested shoot tips immediately and dispose away from the field.",
        "citations": ["Bureau of Plant Industry (DA-BPI) Eggplant Guide", "PCAARRD Eggplant Technology Kit"]
    },
    {
        "id": "kalabasa",
        "name": "Kalabasa (Squash / Pumpkin)",
        "scientific_name": "Cucurbita moschata",
        "family": "Cucurbitaceae (Gourd Family)",
        "local_names": ["Kalabasa", "Squash", "Butternut Squash", "Kusit"],
        "planting_method": "Direct seeding (recommended) or transplanting 12–15 day old seedlings",
        "germination_period": "4–7 days",
        "seedling_age_transplant": "12–15 days (plant gently before roots become root-bound)",
        "ideal_conditions": {
            "temperature": "24°C to 32°C (warm tropical season crop)",
            "soil_type": "Rich, well-draining loam with high organic humus",
            "soil_ph": "6.0 to 7.0",
            "sunlight": "Full sun (at least 6–8 hours direct sunlight)",
            "water_needs": "Moderate; deep watering once or twice a week; avoid wetting foliage to prevent powdery mildew",
            "spacing": "1.0–1.5 meters between hills, 2.0–3.0 meters between rows (or trellised)"
        },
        "days_to_harvest": "75–90 days from planting for tender immature squash or male flowers; 90–110 days for fully mature ripe squash",
        "days_to_maturity": "90–110 days; varieties like Suprema F1 mature in ~85–90 days, while native varieties take 100–110 days",
        "harvesting_guide": "For ripe fruit: stems become corky and dry, rind turns deep orange-tan or mottled dark green and cannot be punctured easily with a thumbnail. Cut with 5 cm stem intact. Male flowers and young shoot tips (talbos ng kalabasa) can be harvested continuously in the morning.",
        "fertilizer_recommendation": {
            "type": "Well-cured compost, Complete 14-14-14, and Potash 0-0-60",
            "nutrients": "High P at planting, moderate N during vine run, and high K during fruit expansion.",
            "timing_method": "Basal: 2 kg compost + 20 g Complete (14-14-14) per hill. Side-dress: At 30 days and 50 days after planting, apply 15 g 14-14-14 + 5 g 0-0-60 in a ring 20 cm around the vine base.",
            "rates_summary": "90–100 kg N, 60 kg P2O5, 90 kg K2O per hectare."
        },
        "growing_tips": "Encourage bee pollination by planting flowering borders; in enclosed home gardens, hand-pollinate female flowers in early morning. Mulch soil beneath vines to prevent ground rot.",
        "citations": ["DA-BPI Squash Production Guidelines", "East-West Seed Suprema Guide"]
    },
    {
        "id": "kamatis",
        "name": "Kamatis (Tomato)",
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae (Nightshade Family)",
        "local_names": ["Kamatis", "Tomato", "Tomate"],
        "planting_method": "Seedling tray propagation followed by transplanting to raised beds",
        "germination_period": "5–8 days",
        "seedling_age_transplant": "25–30 days after sowing (with 4–5 true leaves, thick stem)",
        "ideal_conditions": {
            "temperature": "20°C to 28°C (fruit set drops significantly above 32°C daytime / 22°C nighttime)",
            "soil_type": "Deep, loamy soil with excellent internal drainage and rich compost",
            "soil_ph": "6.0 to 6.8 (adequate calcium prevents blossom end rot)",
            "sunlight": "Full sun (minimum 6–8 hours daily)",
            "water_needs": "Consistent moisture; drip or base watering is ideal; avoid splashing leaves",
            "spacing": "40–50 cm between plants, 75–100 cm between rows"
        },
        "days_to_harvest": "55–70 days from transplanting (or 85–100 days from seed)",
        "days_to_maturity": "75–90 days for determinate varieties (e.g., Diamante Max, Rosas); 90–110 days for indeterminate varieties",
        "harvesting_guide": "Harvest at 'breaker stage' (first blush of pink/red at the blossom end) for transport and shelf-life, or full red ripe for immediate consumption. Gently twist fruit upward from the stem spur.",
        "fertilizer_recommendation": {
            "type": "Organic compost, Complete 14-14-14, Calcium Nitrate, and Muriate of Potash 0-0-60",
            "nutrients": "Moderate N, high P for early root vigor, high K and Calcium for fruit firmness, sweetness, and crack resistance.",
            "timing_method": "Basal: 15 g Complete 14-14-14 + 250 g compost per hill. Side-dress 1: 14 days after transplanting with 5 g Urea + 5 g Potash. Side-dress 2 & 3: Every 15 days during fruiting with 10 g 14-14-14.",
            "rates_summary": "100–140 kg N, 80 kg P2O5, 120 kg K2O per hectare (DA-BPI standard)."
        },
        "growing_tips": "Prune suckers on indeterminate varieties; stake or cage plants early. Add agricultural lime or eggshell powder to acidic soils to ensure calcium availability and avoid blossom end rot.",
        "citations": ["Bureau of Plant Industry (DA-BPI) Tomato Manual", "AVRDC Vegetable Factsheets"]
    },
    {
        "id": "okra",
        "name": "Okra (Lady's Finger)",
        "scientific_name": "Abelmoschus esculentus",
        "family": "Malvaceae (Mallow Family)",
        "local_names": ["Okra", "Gumbo", "Lady's Finger"],
        "planting_method": "Direct seeding (soaking seeds overnight in lukewarm water accelerates sprouting)",
        "germination_period": "4–7 days",
        "seedling_age_transplant": "Direct seeding is preferred due to fragile taproot; if tray-started, transplant within 10–12 days",
        "ideal_conditions": {
            "temperature": "24°C to 35°C (loves heat, sun, and humidity)",
            "soil_type": "Well-drained sandy loam or clay loam with neutral to slightly acidic pH",
            "soil_ph": "6.0 to 6.8",
            "sunlight": "Full sun (minimum 6–8 hours daily)",
            "water_needs": "Moderate; drought-tolerant once established, but regular watering yields tender pods",
            "spacing": "30–40 cm between plants, 75–90 cm between rows"
        },
        "days_to_harvest": "50–60 days from sowing",
        "days_to_maturity": "55–65 days for open-pollinated varieties (e.g., Smooth Green) and hybrids (e.g., Camiling, Lucky 5)",
        "harvesting_guide": "Harvest pods when they are 7–10 cm (3–4 inches) long, tender, and snap cleanly at the tip. Harvest every 2 to 3 days using garden scissors or a sharp knife wearing gloves. If pods become woody or fibrous, cut them off to stimulate new blossoms.",
        "fertilizer_recommendation": {
            "type": "Compost / vermicast, Complete 14-14-14, and Urea 46-0-0",
            "nutrients": "Moderate N (excessive nitrogen creates giant bushy plants with few flowers), high P and K for continuous flower budding.",
            "timing_method": "Basal: 10 g Complete 14-14-14 + 150 g compost per hill. Side-dress: 25–30 days after sowing (at first flowering), apply 5 g Urea + 5 g Complete per hill.",
            "rates_summary": "60–80 kg N, 50 kg P2O5, 60 kg K2O per hectare."
        },
        "growing_tips": "Wear long sleeves when harvesting as okra plant hairs can cause skin irritation. Remove lower leaves below harvested pods to improve aeration and deter fungal pests.",
        "citations": ["DA-BPI Okra Production Guide", "PCARRD Agricultural Information Series"]
    },
    {
        "id": "sili",
        "name": "Sili (Chili Pepper / Bell Pepper)",
        "scientific_name": "Capsicum annuum / Capsicum frutescens",
        "family": "Solanaceae (Nightshade Family)",
        "local_names": ["Siling Labuyo", "Siling Haba / Panigang", "Chili Pepper", "Bell Pepper"],
        "planting_method": "Seedbed / tray germination followed by transplanting to raised beds",
        "germination_period": "7–14 days",
        "seedling_age_transplant": "30–35 days after sowing (4–6 true leaves)",
        "ideal_conditions": {
            "temperature": "22°C to 32°C",
            "soil_type": "Rich, loose sandy loam with organic compost and sharp drainage",
            "soil_ph": "5.8 to 6.8",
            "sunlight": "Full sun (6–8 hours daily)",
            "water_needs": "Moderate; avoid overwatering or waterlogged roots which trigger bacterial wilt",
            "spacing": "40–50 cm between plants, 60–75 cm between rows"
        },
        "days_to_harvest": "60–75 days from transplanting for green hot peppers; 85–100 days for fully ripe red chilies",
        "days_to_maturity": "80–110 days depending on whether harvested green or red-ripe",
        "harvesting_guide": "Cut peppers with a sharp knife or shears leaving 1–2 cm of pedicel (stem). For Siling Labuyo, harvest when pods are bright fiery red. For Siling Haba (finger pepper), harvest when pods are firm, glossy green, and 12–15 cm long.",
        "fertilizer_recommendation": {
            "type": "Organic compost, Complete 14-14-14, Urea 46-0-0, Muriate of Potash 0-0-60",
            "nutrients": "Balanced NPK early; elevated Potassium and Calcium during flowering and pod development.",
            "timing_method": "Basal: 15 g Complete 14-14-14 + 200 g compost per hill. Side-dress: Apply 5 g Urea + 5 g Potash at 14 days and 35 days after transplanting.",
            "rates_summary": "100–120 kg N, 60–80 kg P2O5, 80–100 kg K2O per hectare."
        },
        "growing_tips": "Pinch off the first flower bud at the central fork to encourage lateral branching and higher total yield. Protect against thrips and mites using yellow sticky traps and neem oil.",
        "citations": ["DA-BPI Pepper Production Guide", "PCAARRD Sili Technology Pack"]
    },
    {
        "id": "kangkong",
        "name": "Kangkong (Water Spinach / Swamp Cabbage)",
        "scientific_name": "Ipomoea aquatica",
        "family": "Convolvulaceae (Morning Glory Family)",
        "local_names": ["Kangkong", "Water Spinach", "Swamp Cabbage", "Ong Choy"],
        "planting_method": "Direct seeding or stem cuttings (upland and lowland cultivation)",
        "germination_period": "3–5 days (soaking seeds for 24 hours boosts germination)",
        "seedling_age_transplant": "Usually direct seeded; if transplanted, 10–12 days",
        "ideal_conditions": {
            "temperature": "25°C to 35°C (highly tropical, warm, moisture-loving)",
            "soil_type": "Moist, rich loam or clay loam with high organic matter; upland beds or hydroponic beds",
            "soil_ph": "5.5 to 7.0",
            "sunlight": "Full sun to moderate partial shade",
            "water_needs": "High; requires consistently wet or moist soil; can tolerate flooded/waterlogged beds",
            "spacing": "10–15 cm between plants, 20 cm between rows"
        },
        "days_to_harvest": "25–35 days from sowing (or 20 days from stem cuttings)",
        "days_to_maturity": "30–40 days to full tender foliage maturity",
        "harvesting_guide": "Cut young tender shoot tips (15–20 cm) leaving 5 cm of basal stem with 2–3 nodes. Plants will rapidly sprout new lateral shoots, allowing repeat harvesting every 10–14 days for 3–4 months.",
        "fertilizer_recommendation": {
            "type": "High-nitrogen organic compost, fermented plant juice (FPJ), Complete 14-14-14, and Urea 46-0-0",
            "nutrients": "Very high Nitrogen demand to fuel rapid foliage and tender stem production.",
            "timing_method": "Basal: Incorporate 1 kg compost per m² + 15 g Complete 14-14-14. Side-dress: Dissolve 10 g Urea per 10 L of water and drench bed every 10 days after each harvest cut.",
            "rates_summary": "80–100 kg N per hectare equivalent."
        },
        "growing_tips": "Ideal for container gardening, hydroponics, or wet garden corners. Keep soil perpetually moist to ensure tender stems and prevent bitterness.",
        "citations": ["DA-BPI Leafy Vegetable Guide - Kangkong", "FAO Traditional Vegetables Manual"]
    },
    {
        "id": "repolyo",
        "name": "Repolyo (Cabbage)",
        "scientific_name": "Brassica oleracea var. capitata",
        "family": "Brassicaceae (Mustard / Cabbage Family)",
        "local_names": ["Repolyo", "Cabbage", "Head Cabbage"],
        "planting_method": "Seedling tray propagation followed by transplanting to raised beds",
        "germination_period": "4–7 days",
        "seedling_age_transplant": "25–30 days after sowing (4–5 true leaves)",
        "ideal_conditions": {
            "temperature": "15°C to 24°C (thrives in high-elevation areas like Benguet, Bukidnon; heat-tolerant lowland hybrids available)",
            "soil_type": "Deep, well-draining, fertile clay-loam high in organic matter",
            "soil_ph": "6.0 to 6.8",
            "sunlight": "Full sunlight (minimum 6 hours)",
            "water_needs": "Moderate and uniform; irregular watering causes head cracking",
            "spacing": "35–45 cm between plants, 50–60 cm between rows"
        },
        "days_to_harvest": "60–75 days from transplanting (or 85–105 days from sowing)",
        "days_to_maturity": "75–95 days depending on the cultivar (early hybrids like KK Cross mature in ~60 days after transplanting, late storage varieties take 85+ days)",
        "harvesting_guide": "Harvest when heads feel firm, compact, and solid when gently squeezed. Cut head cleanly at the base with a sharp knife, retaining 2–3 outer wrapper leaves for protection.",
        "fertilizer_recommendation": {
            "type": "Organic compost, Complete 14-14-14, Urea 46-0-0, Muriate of Potash 0-0-60",
            "nutrients": "High Nitrogen for frame development, followed by high Potassium during head formation and tightening.",
            "timing_method": "Basal: 20 g Complete 14-14-14 + 300 g compost per plant. Side-dress 1: 15 days after transplanting with 5 g Urea. Side-dress 2: 35 days after transplanting with 5 g Urea + 5 g Potash.",
            "rates_summary": "150 kg N, 90 kg P2O5, 120 kg K2O per hectare (Benguet State Univ / DA-BPI)."
        },
        "growing_tips": "Avoid water stress during head formation. Scout regularly for diamondback moth (DBM); use Bacillus thuringiensis (Bt) or companion intercropping with dill or mint.",
        "citations": ["DA-CAR Highland Vegetable Technical Guide", "PCARRD Cabbage Manual"]
    },
    {
        "id": "carrots",
        "name": "Carrots",
        "scientific_name": "Daucus carota subsp. sativus",
        "family": "Apiaceae (Umbelliferae / Carrot Family)",
        "local_names": ["Karot", "Carrot", "Zanahoria"],
        "planting_method": "Direct seeding only (transplanting causes root forking and deformation)",
        "germination_period": "7–14 days (seeds require consistent moisture to germinate)",
        "seedling_age_transplant": "Not applicable (never transplant root crops)",
        "ideal_conditions": {
            "temperature": "16°C to 22°C (cool climates like Benguet/Dalwangan or cool season lowland)",
            "soil_type": "Deep, loose, stone-free, sandy loam soil tilled to at least 30 cm depth",
            "soil_ph": "6.0 to 6.8",
            "sunlight": "Full sun (6–8 hours daily)",
            "water_needs": "Consistent light watering; fluctuating moisture causes split and cracked roots",
            "spacing": "5–8 cm between plants after thinning, 20–25 cm between drill rows"
        },
        "days_to_harvest": "75–90 days from sowing",
        "days_to_maturity": "80–100 days; baby carrot varieties ready in ~60–65 days, standard Nantes/Chantenay in ~80–90 days",
        "harvesting_guide": "Harvest when root shoulders reach 2–3 cm diameter and push slightly above the soil surface with vivid orange color. Loosen soil with a hand fork and pull roots by the crown.",
        "fertilizer_recommendation": {
            "type": "Well-aged compost (never fresh manure!), Complete 14-14-14, and Potash 0-0-60",
            "nutrients": "Moderate Nitrogen (excess N causes hairy, forked roots and leafy tops), high Phosphorus and high Potassium for root elongation and sugar synthesis.",
            "timing_method": "Basal: Thoroughly incorporate 15 g Complete 14-14-14 per meter of row at planting. Side-dress: 30 days after sowing with 5 g Potash + 3 g Urea per meter row.",
            "rates_summary": "60–80 kg N, 80 kg P2O5, 100 kg K2O per hectare."
        },
        "growing_tips": "Thin seedlings when 5 cm tall to prevent crowded misshapen roots. Ensure soil is completely free of stones, gravel, and unrotted organic matter.",
        "citations": ["DA-BPI Root Crops Guide", "FAO Carrot Production Manual"]
    },
    {
        "id": "lettuce",
        "name": "Lettuce (Leaf, Romaine, Butterhead)",
        "scientific_name": "Lactuca sativa",
        "family": "Asteraceae (Daisy / Sunflower Family)",
        "local_names": ["Letsugas", "Lettuce", "Salad Greens"],
        "planting_method": "Transplanting or direct seeding (transplanting in plug trays produces superior heads)",
        "germination_period": "3–6 days (needs light to germinate; surface sow or cover very lightly with 2 mm fine soil)",
        "seedling_age_transplant": "14–18 days after sowing (3–4 true leaves)",
        "ideal_conditions": {
            "temperature": "16°C to 24°C (heat-tolerant loose-leaf varieties like Lollo Bionda, Rapid Green perform well in tropics with 30% shade net)",
            "soil_type": "Rich, moisture-retentive, loose loamy soil with plenty of organic matter",
            "soil_ph": "6.0 to 7.0",
            "sunlight": "Full sun in cool season; 30–50% shade cloth during hot tropical mid-day",
            "water_needs": "Frequent shallow watering; shallow root system is sensitive to drought",
            "spacing": "20–25 cm between plants, 25–30 cm between rows"
        },
        "days_to_harvest": "35–45 days from sowing for loose-leaf types (or 25–30 days after transplanting); 50–65 days for heading/romaine types",
        "days_to_maturity": "40–60 days depending on variety and temperature",
        "harvesting_guide": "Harvest loose-leaf types leaf-by-leaf (cut-and-come-again) or cut whole heads early in the morning before sun warms the leaves. Harvest before flower stalks initiate to avoid milky bitter sap.",
        "fertilizer_recommendation": {
            "type": "Vermicompost, balanced organic liquid fertilizer, Complete 14-14-14, and Urea",
            "nutrients": "High Nitrogen for succulent tender leaves, adequate Phosphorus for root network, moderate Potassium.",
            "timing_method": "Basal: 1 kg vermicompost + 10 g Complete 14-14-14 per m². Side-dress: Liquid feed with compost tea or dilute Urea (5 g/L) every 10 days.",
            "rates_summary": "80–100 kg N, 50 kg P2O5, 60 kg K2O per hectare."
        },
        "growing_tips": "Ideal for hydroponics (NFT, Kratky) and container gardens. Keep root zone cool with straw mulch to prevent bolting (premature flowering).",
        "citations": ["DA-BPI Lettuce Guidelines", "University Extension Vegetable Publications"]
    },
    {
        "id": "pipino",
        "name": "Pipino (Cucumber)",
        "scientific_name": "Cucumis sativus",
        "family": "Cucurbitaceae (Gourd Family)",
        "local_names": ["Pipino", "Cucumber", "Pepino"],
        "planting_method": "Direct seeding or seedling tray transplanting onto trellised beds",
        "germination_period": "3–6 days",
        "seedling_age_transplant": "10–14 days (transplant before taproot circles)",
        "ideal_conditions": {
            "temperature": "22°C to 32°C",
            "soil_type": "Fertile, loose, well-draining sandy loam rich in organic matter",
            "soil_ph": "6.0 to 6.8",
            "sunlight": "Full sunlight (minimum 6 hours daily)",
            "water_needs": "High and steady; water stress causes bitter fruit and misshapen tapering",
            "spacing": "30–40 cm between plants, 1.2–1.5 meters between trellised rows"
        },
        "days_to_harvest": "40–50 days from sowing (or 30–35 days from transplanting)",
        "days_to_maturity": "45–55 days for slicing/salad varieties; 40–45 days for pickling varieties",
        "harvesting_guide": "Harvest when fruits are firm, uniform green, 15–20 cm long with rounded ends before seeds harden or rind yellows. Harvest every 2 days using a sharp knife; prompt harvesting stimulates ongoing flower and fruit production.",
        "fertilizer_recommendation": {
            "type": "Organic compost, Complete 14-14-14, Urea 46-0-0, and Muriate of Potash 0-0-60",
            "nutrients": "Moderate N, high P at root stage, high K during rapid fruit growth.",
            "timing_method": "Basal: 15 g Complete 14-14-14 + 200 g compost per hill. Side-dress: 10 g 14-14-14 + 5 g Urea per hill every 14 days after flowering commences.",
            "rates_summary": "100 kg N, 60 kg P2O5, 90 kg K2O per hectare."
        },
        "growing_tips": "Train vines on a 1.8-meter trellis to keep cucumbers straight, clean, and free of ground rot. Irrigate at the soil level to prevent downy mildew on leaves.",
        "citations": ["DA-BPI Cucumber Production Manual", "East-West Seed Cucumber Guide"]
    },
    {
        "id": "labanos",
        "name": "Labanos (Radish / Daikon)",
        "scientific_name": "Raphanus sativus var. longipinnatus",
        "family": "Brassicaceae (Mustard / Cabbage Family)",
        "local_names": ["Labanos", "Radish", "Daikon", "White Radish"],
        "planting_method": "Direct seeding only (never transplant)",
        "germination_period": "3–5 days",
        "seedling_age_transplant": "Not applicable (direct seeding preserves straight taproot)",
        "ideal_conditions": {
            "temperature": "18°C to 28°C (fast-growing cool-to-mild season crop)",
            "soil_type": "Deep, loose, stone-free friable sandy loam",
            "soil_ph": "6.0 to 7.0",
            "sunlight": "Full sun (6+ hours daily)",
            "water_needs": "Even moisture; dry periods followed by heavy watering cause root cracking and pithiness",
            "spacing": "10–15 cm between plants after thinning, 25–30 cm between rows"
        },
        "days_to_harvest": "35–50 days from sowing",
        "days_to_maturity": "40–55 days (varieties like '60 Days' or 'Minowase Summer Cross')",
        "harvesting_guide": "Harvest when roots reach 20–30 cm long and 3–5 cm in diameter while still crisp and solid. Do not delay harvest or roots will become pithy, woody, and intensely pungent.",
        "fertilizer_recommendation": {
            "type": "Aged compost, Complete 14-14-14, and Potash 0-0-60",
            "nutrients": "Low Nitrogen (excess N causes leafy foliage with skinny hollow roots); high Phosphorus and Potassium for root density.",
            "timing_method": "Basal: 15 g Complete 14-14-14 per meter row mixed thoroughly into soil. Side-dress: 20 days after sowing with 5 g Potash per meter row.",
            "rates_summary": "50 kg N, 60 kg P2O5, 80 kg K2O per hectare."
        },
        "growing_tips": "Thin seedlings early (at 7–10 days) to prevent crowded deformities. Keep beds weed-free during the first 3 weeks.",
        "citations": ["DA-BPI Radish Guide", "PCAARRD Root Crop Handbooks"]
    }
]

def get_vegetable_by_id(veg_id: str):
    veg_id_clean = veg_id.strip().lower()
    for veg in VEGETABLE_DATA:
        if veg["id"] == veg_id_clean:
            return veg
    return None

def search_vegetables(query: str):
    query_lower = query.strip().lower()
    matches = []
    for veg in VEGETABLE_DATA:
        names = [veg["name"].lower(), veg["scientific_name"].lower()] + [n.lower() for n in veg["local_names"]]
        if any(query_lower in name for name in names):
            matches.append(veg)
    return matches
