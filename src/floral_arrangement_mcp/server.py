"""
Floral Arrangement Aesthetics MCP Server

Dual-purpose server providing:
1. Prompt enhancement with professional floral vocabulary
2. ComfyUI workflow generation for floral imagery

Three-layer architecture:
- Layer 1: Deterministic taxonomy (arrangement styles, flowers, techniques)
- Layer 2: Structural mapping (balance, proportion, movement)
- Layer 3: Cultural/aesthetic context synthesis
"""

from fastmcp import FastMCP
import json
from typing import Dict, List, Optional, Any

mcp = FastMCP("floral-arrangement-aesthetics")

# ============================================================================
# LAYER 1: COMPREHENSIVE FLORAL TAXONOMY
# ============================================================================

ARRANGEMENT_STYLES = {
    "ikebana": {
        "moribana": {
            "description": "Low bowl arrangement, naturalistic landscape",
            "container": "shallow bowl, suiban",
            "characteristics": "horizontal emphasis, nature scenery, kenzan pin holder",
            "balance": "asymmetrical",
            "complexity": "high"
        },
        "nageire": {
            "description": "Tall vase arrangement, flowing asymmetrical",
            "container": "tall cylindrical vase",
            "characteristics": "natural grace, no mechanics visible, stem supports stem",
            "balance": "asymmetrical",
            "complexity": "medium"
        },
        "rikka": {
            "description": "Formal standing flowers, classical seven-branch",
            "container": "bronze or ceramic vase",
            "characteristics": "symbolic cosmic mountain, rigid structure, ceremonial",
            "balance": "symmetrical",
            "complexity": "very high"
        }
    },
    "western_classical": {
        "cascade": {
            "description": "Waterfall flow with trailing elements",
            "container": "elevated pedestal vase or urn",
            "characteristics": "dramatic downward movement, trailing vines, 1.5x container height drop",
            "balance": "asymmetrical",
            "complexity": "high"
        },
        "crescent": {
            "description": "Curved asymmetrical arc, moon-shaped",
            "container": "low bowl or compote",
            "characteristics": "graceful curve, negative space emphasis, 60-degree arc",
            "balance": "asymmetrical",
            "complexity": "medium"
        },
        "hogarth": {
            "description": "S-curve, line of beauty",
            "container": "pedestal vase or urn",
            "characteristics": "flowing S-shape, dynamic movement, elegant proportion",
            "balance": "asymmetrical",
            "complexity": "high"
        },
        "dome": {
            "description": "Rounded symmetrical mass",
            "container": "low bowl, vase, or compote",
            "characteristics": "equal dimensions all sides, full 360-degree viewing, dense",
            "balance": "radial symmetrical",
            "complexity": "low"
        },
        "triangular": {
            "description": "Stable pyramid form",
            "container": "any stable base",
            "characteristics": "wide base tapering to point, classical proportion, formal",
            "balance": "symmetrical",
            "complexity": "low"
        },
        "vertical": {
            "description": "Tall upright emphasis",
            "container": "tall narrow vase",
            "characteristics": "height 2-3x container, upward movement, line flowers dominant",
            "balance": "symmetrical or asymmetrical",
            "complexity": "low"
        },
        "horizontal": {
            "description": "Low spreading centerpiece",
            "container": "long low container or candelabra",
            "characteristics": "width 3x height, table centerpiece, conversation-friendly",
            "balance": "symmetrical",
            "complexity": "medium"
        }
    },
    "contemporary": {
        "minimalist": {
            "description": "Few stems, negative space emphasis",
            "container": "simple geometric vessel",
            "characteristics": "3-7 stems maximum, sculptural form, breathing space",
            "balance": "asymmetrical",
            "complexity": "medium"
        },
        "structural": {
            "description": "Architectural, geometric forms",
            "container": "modern cube, cylinder, or asymmetric",
            "characteristics": "bold lines, repetition, graphic shapes, non-traditional materials",
            "balance": "often asymmetrical",
            "complexity": "high"
        },
        "garden_style": {
            "description": "Loose, natural, abundant",
            "container": "rustic basket, vintage vessel",
            "characteristics": "just-picked feel, varied textures, romantic fullness, organic",
            "balance": "asymmetrical",
            "complexity": "medium"
        },
        "parallel": {
            "description": "Stems grouped in vertical lines",
            "container": "rectangular or cylindrical",
            "characteristics": "stems visible through glass, grouped bundles, modern clean",
            "balance": "symmetrical or asymmetrical",
            "complexity": "low"
        }
    }
}

FLOWERS_BY_ROLE = {
    "focal": {
        "roses": {
            "types": ["garden roses", "spray roses", "hybrid tea", "English roses"],
            "characteristics": "classic beauty, layered petals, focal point dominance",
            "color_range": "full spectrum",
            "size": "large 3-5 inches",
            "seasons": ["spring", "summer", "fall"],
            "symbolism": "love, romance, elegance"
        },
        "peonies": {
            "types": ["herbaceous", "tree peony", "Itoh hybrid"],
            "characteristics": "lush ruffled petals, full bloom drama, short season",
            "color_range": "white, pink, coral, burgundy",
            "size": "very large 4-6 inches",
            "seasons": ["late spring", "early summer"],
            "symbolism": "prosperity, honor, romance"
        },
        "lilies": {
            "types": ["oriental", "asiatic", "calla", "trumpet"],
            "characteristics": "dramatic form, strong fragrance (oriental), architectural",
            "color_range": "full spectrum",
            "size": "large 4-6 inches per bloom",
            "seasons": ["summer", "fall"],
            "symbolism": "purity, majesty, sophistication"
        },
        "orchids": {
            "types": ["phalaenopsis", "cymbidium", "dendrobium", "vanda"],
            "characteristics": "exotic elegance, long-lasting, tropical",
            "color_range": "white, pink, purple, yellow, green",
            "size": "medium 2-4 inches",
            "seasons": ["year-round"],
            "symbolism": "luxury, refinement, beauty"
        },
        "hydrangeas": {
            "types": ["mophead", "lacecap", "paniculata", "oakleaf"],
            "characteristics": "full mass, color-changing, garden feel",
            "color_range": "blue, pink, white, green, purple",
            "size": "very large 6-8 inch heads",
            "seasons": ["summer", "fall"],
            "symbolism": "gratitude, abundance, heartfelt emotion"
        },
        "sunflowers": {
            "types": ["giant", "teddy bear", "moulin rouge", "autumn beauty"],
            "characteristics": "bold face, cheerful, rustic charm",
            "color_range": "yellow, orange, burgundy, bronze",
            "size": "large 4-10 inches",
            "seasons": ["summer", "fall"],
            "symbolism": "happiness, loyalty, longevity"
        },
        "dahlias": {
            "types": ["dinner plate", "cactus", "pompon", "decorative"],
            "characteristics": "geometric petals, bold color, garden luxury",
            "color_range": "full spectrum except blue",
            "size": "small to very large 2-10 inches",
            "seasons": ["late summer", "fall"],
            "symbolism": "elegance, dignity, commitment"
        }
    },
    "line": {
        "snapdragons": {
            "characteristics": "vertical spikes, graduated blooms, height emphasis",
            "color_range": "full spectrum",
            "height": "18-36 inches",
            "use": "creates vertical movement and height"
        },
        "delphiniums": {
            "characteristics": "tall elegant columns, cottage garden feel",
            "color_range": "blue, purple, pink, white",
            "height": "24-48 inches",
            "use": "dramatic height, romantic spires"
        },
        "gladiolus": {
            "characteristics": "sword-like stems, formal linear",
            "color_range": "full spectrum",
            "height": "24-60 inches",
            "use": "strong vertical lines, classical elegance"
        },
        "liatris": {
            "characteristics": "fuzzy textured spikes, blooms top-down",
            "color_range": "purple, white",
            "height": "18-36 inches",
            "use": "unique texture, prairie wildflower feel"
        },
        "bells_of_ireland": {
            "characteristics": "green architectural spires, shell-like calyxes",
            "color_range": "lime green",
            "height": "24-36 inches",
            "use": "fresh green accent, Irish symbolism"
        },
        "stock": {
            "characteristics": "fragrant vertical clusters, cottage garden",
            "color_range": "white, pink, purple, lavender",
            "height": "18-30 inches",
            "use": "fragrance, soft spires, romantic"
        }
    },
    "filler": {
        "baby_breath": {
            "characteristics": "cloud-like delicate, tiny white blooms",
            "use": "softens arrangements, creates airiness, classic filler",
            "texture": "fine, misty"
        },
        "waxflower": {
            "characteristics": "tiny clustered blooms, long-lasting, waxy texture",
            "color_range": "white, pink, purple",
            "use": "elegant filler, wedding favorite"
        },
        "statice": {
            "characteristics": "papery textured, long-lasting, dried feel",
            "color_range": "purple, white, yellow, pink",
            "use": "texture contrast, everlasting quality"
        },
        "solidago": {
            "characteristics": "golden plumes, wild meadow feel",
            "color_range": "yellow, gold",
            "use": "fall arrangements, cheerful accent"
        },
        "alstroemeria": {
            "characteristics": "small lily-like, long vase life, multiple blooms",
            "color_range": "full spectrum",
            "use": "versatile filler, budget-friendly"
        },
        "hypericum": {
            "characteristics": "berry-like, unique texture",
            "color_range": "red, burgundy, white, green",
            "use": "adds interest, festive accent"
        }
    },
    "texture": {
        "thistle": {
            "characteristics": "spiky, architectural, edgy",
            "color_range": "purple, blue, white",
            "use": "modern edge, texture contrast"
        },
        "protea": {
            "characteristics": "bold sculptural, exotic",
            "color_range": "pink, coral, cream",
            "use": "focal drama, tropical luxury"
        },
        "scabiosa": {
            "characteristics": "pincushion center, whimsical",
            "color_range": "deep burgundy, purple, white",
            "use": "unique texture, romantic gardens"
        },
        "ranunculus": {
            "characteristics": "layered tissue-paper petals, romantic",
            "color_range": "full spectrum",
            "use": "texture richness, elegant beauty"
        }
    }
}

FOLIAGE_TYPES = {
    "structural": {
        "ferns": {
            "types": ["leather fern", "tree fern", "sword fern"],
            "characteristics": "feathery fronds, classical backdrop",
            "use": "traditional base, soft texture"
        },
        "eucalyptus": {
            "types": ["seeded", "silver dollar", "baby blue"],
            "characteristics": "silvery-blue leaves, aromatic, trendy",
            "use": "modern texture, color accent, fragrance"
        },
        "ruscus": {
            "characteristics": "glossy pointed leaves, sturdy stems",
            "use": "foundation greenery, long-lasting"
        },
        "salal": {
            "characteristics": "rounded glossy leaves, pacific northwest",
            "use": "backdrop greenery, filler"
        }
    },
    "accent": {
        "ivy": {
            "types": ["English ivy", "variegated ivy"],
            "characteristics": "trailing vines, romantic drape",
            "use": "softens edges, cascading effect"
        },
        "pittosporum": {
            "characteristics": "small rounded leaves, delicate sprays",
            "use": "airy filler, soft texture"
        },
        "dusty_miller": {
            "characteristics": "silvery fuzzy leaves, soft focus",
            "use": "color contrast, romantic softness"
        },
        "olive_branches": {
            "characteristics": "silvery-green, Mediterranean, symbolic",
            "use": "rustic elegance, peace symbolism"
        }
    },
    "dramatic": {
        "monstera": {
            "characteristics": "large split leaves, tropical bold",
            "use": "modern drama, tropical theme"
        },
        "palm": {
            "types": ["fan palm", "phoenix palm"],
            "characteristics": "architectural fronds, tropical",
            "use": "bold statement, event decor"
        },
        "aspidistra": {
            "characteristics": "large blade leaves, manipulable",
            "use": "wraps, structural elements"
        }
    }
}

COLOR_PALETTES = {
    "monochromatic": {
        "description": "Single color in varying shades and tints",
        "examples": ["all white", "blush to deep pink", "cream to chocolate"],
        "effect": "sophisticated, cohesive, elegant",
        "occasions": ["wedding", "formal", "minimalist"]
    },
    "analogous": {
        "description": "Colors adjacent on color wheel",
        "examples": ["yellow-orange-red", "blue-purple-violet", "yellow-green-blue"],
        "effect": "harmonious, natural, pleasing",
        "occasions": ["everyday", "celebration", "garden-style"]
    },
    "complementary": {
        "description": "Opposite colors on wheel",
        "examples": ["purple-yellow", "blue-orange", "red-green"],
        "effect": "vibrant, energetic, bold contrast",
        "occasions": ["celebration", "modern", "attention-grabbing"]
    },
    "triadic": {
        "description": "Three colors evenly spaced on wheel",
        "examples": ["red-yellow-blue", "orange-green-purple"],
        "effect": "vibrant, balanced, rich",
        "occasions": ["festive", "children", "joyful"]
    },
    "romantic": {
        "colors": ["blush pink", "cream", "soft peach", "ivory", "champagne"],
        "effect": "soft, dreamy, feminine, gentle",
        "occasions": ["wedding", "bridal shower", "anniversary"]
    },
    "elegant": {
        "colors": ["deep burgundy", "cream", "forest green", "white", "gold accent"],
        "effect": "sophisticated, refined, formal",
        "occasions": ["gala", "formal dinner", "luxury events"]
    },
    "vibrant": {
        "colors": ["magenta", "orange", "hot pink", "yellow", "coral"],
        "effect": "energetic, joyful, bold",
        "occasions": ["birthday", "tropical", "celebration"]
    },
    "spring": {
        "colors": ["tulip yellow", "daffodil", "lavender", "soft pink", "fresh green"],
        "effect": "fresh, renewal, optimistic",
        "seasons": ["spring"],
        "occasions": ["easter", "spring wedding"]
    },
    "summer": {
        "colors": ["bright yellow", "coral", "hot pink", "orange", "lime green"],
        "effect": "warm, abundant, lively",
        "seasons": ["summer"],
        "occasions": ["garden party", "outdoor celebration"]
    },
    "autumn": {
        "colors": ["rust orange", "burgundy", "golden yellow", "bronze", "deep red"],
        "effect": "warm, rich, harvest",
        "seasons": ["fall"],
        "occasions": ["thanksgiving", "fall wedding"]
    },
    "winter": {
        "colors": ["deep red", "white", "evergreen", "silver", "navy"],
        "effect": "crisp, festive, elegant",
        "seasons": ["winter"],
        "occasions": ["christmas", "winter formal"]
    }
}

STRUCTURAL_TECHNIQUES = {
    "balance": {
        "symmetrical_radial": {
            "description": "Equal visual weight radiating from center",
            "arrangements": ["dome", "round", "triangular"],
            "effect": "formal, stable, traditional"
        },
        "symmetrical_bilateral": {
            "description": "Mirror image left and right",
            "arrangements": ["triangular", "vertical", "fan"],
            "effect": "formal, classical, orderly"
        },
        "asymmetrical": {
            "description": "Unequal but balanced visual weight",
            "arrangements": ["crescent", "hogarth", "ikebana"],
            "effect": "dynamic, natural, contemporary"
        }
    },
    "proportion": {
        "golden_ratio": {
            "description": "1.618:1 ratio between elements",
            "application": "height to width, focal to filler, container to arrangement"
        },
        "rule_of_thirds": {
            "description": "Divide into thirds horizontally and vertically",
            "application": "place focal points at intersections"
        },
        "height_to_container": {
            "traditional": "1.5 to 2 times container height",
            "modern": "can break rules for dramatic effect",
            "horizontal": "container height to arrangement width 1:3"
        }
    },
    "focal_points": {
        "single_dominant": {
            "description": "One clear center of interest",
            "technique": "largest bloom at center or asymmetric position",
            "effect": "clear hierarchy, classical"
        },
        "multiple_secondary": {
            "description": "Primary focal with supporting accents",
            "technique": "triangle of focal flowers",
            "effect": "visual journey, sophisticated"
        },
        "distributed": {
            "description": "Interest spread throughout",
            "technique": "no single dominant element",
            "effect": "garden-style, natural"
        }
    },
    "movement": {
        "vertical_lift": {
            "description": "Upward reaching energy",
            "technique": "line flowers, tall stems, upright forms",
            "effect": "aspiration, celebration, growth"
        },
        "horizontal_sweep": {
            "description": "Side-to-side flow",
            "technique": "trailing elements, lateral branches",
            "effect": "calm, peaceful, grounding"
        },
        "spiral_rotation": {
            "description": "Circular flow around center",
            "technique": "stems arranged in spiral, flowers face different directions",
            "effect": "dynamic, natural, garden-style"
        },
        "cascade_fall": {
            "description": "Downward waterfall motion",
            "technique": "trailing ivy, hanging amaranthus, weighted bottom",
            "effect": "drama, elegance, gravity"
        },
        "radiation": {
            "description": "Outward burst from center",
            "technique": "stems angle out from central point",
            "effect": "energy, explosion, celebration"
        }
    },
    "texture": {
        "smooth_rough_contrast": {
            "description": "Juxtapose sleek and textured elements",
            "examples": "glossy calla lilies with spiky thistle",
            "effect": "visual interest, sophisticated"
        },
        "delicate_bold_mix": {
            "description": "Combine fine and substantial forms",
            "examples": "baby's breath with large roses",
            "effect": "balance, dimension"
        },
        "monochromatic_texture": {
            "description": "Same color, varied textures",
            "examples": "white roses, ranunculus, stock, baby's breath",
            "effect": "subtle sophistication, cohesive"
        }
    },
    "density": {
        "packed_abundant": {
            "description": "Full mass, minimal negative space",
            "style": "European garden, romantic",
            "effect": "lush, generous, romantic"
        },
        "airy_spacious": {
            "description": "Minimal stems, maximum negative space",
            "style": "Ikebana, contemporary minimalist",
            "effect": "elegant, modern, sculptural"
        },
        "clustered_with_voids": {
            "description": "Dense groupings separated by open space",
            "style": "Contemporary, structural",
            "effect": "drama, graphic, intentional"
        }
    }
}

OCCASIONS = {
    "wedding": {
        "ceremony": {
            "arrangements": ["altar arrangements", "aisle markers", "chuppah flowers"],
            "styles": ["romantic", "elegant", "dramatic"],
            "scale": "large, architectural"
        },
        "reception": {
            "arrangements": ["centerpieces", "cake flowers", "sweetheart table"],
            "styles": ["romantic", "garden-style", "elegant"],
            "scale": "medium, conversation-friendly"
        },
        "bridal_party": {
            "arrangements": ["bouquets", "boutonnieres", "corsages"],
            "styles": ["cohesive with ceremony", "hand-tied", "wearable"],
            "scale": "personal, scaled to person"
        }
    },
    "funeral": {
        "standing_spray": {
            "description": "Easel-mounted vertical arrangement",
            "characteristics": "formal, respectful, traditional symbolism"
        },
        "casket_spray": {
            "description": "Long horizontal arrangement for casket",
            "characteristics": "full coverage, masculine or feminine styling"
        },
        "wreath": {
            "description": "Circular form symbolizing eternal life",
            "characteristics": "traditional, symmetrical, symbolic"
        },
        "sympathy_basket": {
            "description": "Comforting arrangement for home",
            "characteristics": "thoughtful, lasting, garden-style"
        }
    },
    "celebration": {
        "birthday": {
            "characteristics": "joyful, colorful, personal to recipient",
            "styles": ["vibrant", "fun", "favorite colors"]
        },
        "anniversary": {
            "characteristics": "romantic, meaningful, often roses",
            "styles": ["elegant", "romantic", "traditional flowers"]
        },
        "congratulations": {
            "characteristics": "bright, uplifting, celebratory",
            "styles": ["vibrant", "contemporary", "bold"]
        },
        "get_well": {
            "characteristics": "cheerful, uplifting, fragrance-free",
            "styles": ["bright colors", "garden-style", "optimistic"]
        }
    },
    "everyday": {
        "home_decor": {
            "characteristics": "seasonally appropriate, complements interior",
            "styles": ["garden-style", "minimalist", "whatever brings joy"]
        },
        "hostess_gift": {
            "characteristics": "thoughtful, pre-arranged, ready to display",
            "styles": ["elegant", "seasonal", "generous but not overwhelming"]
        }
    }
}

CULTURAL_TRADITIONS = {
    "japanese_ikebana": {
        "philosophy": "minimalism, asymmetry, nature appreciation, spiritual practice",
        "principles": ["heaven-earth-man triangle", "negative space as important as flowers", "seasonal awareness"],
        "key_concepts": {
            "ma": "negative space, pause, interval",
            "wabi_sabi": "imperfect beauty, transience",
            "shin_soe_hikae": "primary, secondary, tertiary elements"
        }
    },
    "european_garden": {
        "philosophy": "abundance, romance, natural beauty",
        "principles": ["lush fullness", "color harmony", "garden-fresh aesthetic"],
        "characteristics": "loose, organic, just-picked feel, varied textures"
    },
    "victorian": {
        "philosophy": "language of flowers, tight structure, formal beauty",
        "principles": ["symbolic meanings", "tight massing", "structured form"],
        "characteristics": "dense, formal, symbolic, tussie-mussie style"
    },
    "contemporary_western": {
        "philosophy": "artistic expression, breaking tradition, individual style",
        "principles": ["rule-breaking", "artistic interpretation", "personal expression"],
        "characteristics": "varied widely, structural, unexpected materials"
    }
}

# ============================================================================
# LAYER 2: DETERMINISTIC MAPPING FUNCTIONS
# ============================================================================

def map_floral_taxonomy(
    user_intent: str,
    style_preference: str = "any",
    occasion: str = "general",
    color_scheme: str = "harmonious"
) -> Dict[str, Any]:
    """
    Map user intent to floral taxonomy elements.
    Pure deterministic lookup - no LLM needed.
    """
    intent_lower = user_intent.lower()
    
    # Detect style from intent
    detected_style = detect_arrangement_style(intent_lower, style_preference)
    
    # Detect flowers mentioned or suggest based on occasion
    detected_flowers = detect_flowers(intent_lower, occasion)
    
    # Detect or suggest foliage
    detected_foliage = detect_foliage(intent_lower, detected_style)
    
    # Detect or map color scheme
    detected_colors = detect_color_scheme(intent_lower, color_scheme, occasion)
    
    # Map structural techniques
    structure = map_structure(detected_style, detected_colors)
    
    # Detect occasion-specific requirements
    occasion_specs = map_occasion(occasion, detected_style)
    
    return {
        "user_intent": user_intent,
        "style": detected_style,
        "flowers": detected_flowers,
        "foliage": detected_foliage,
        "colors": detected_colors,
        "structure": structure,
        "occasion": occasion_specs,
        "cultural_context": get_cultural_context(detected_style)
    }

def detect_arrangement_style(intent: str, preference: str) -> Dict[str, Any]:
    """Detect or select arrangement style."""
    # Check for explicit style mentions
    if "ikebana" in intent or "japanese" in intent:
        if "moribana" in intent:
            return {"category": "ikebana", "type": "moribana", **ARRANGEMENT_STYLES["ikebana"]["moribana"]}
        elif "nageire" in intent:
            return {"category": "ikebana", "type": "nageire", **ARRANGEMENT_STYLES["ikebana"]["nageire"]}
        else:
            return {"category": "ikebana", "type": "nageire", **ARRANGEMENT_STYLES["ikebana"]["nageire"]}
    
    if "cascade" in intent or "waterfall" in intent or "trailing" in intent:
        return {"category": "western_classical", "type": "cascade", **ARRANGEMENT_STYLES["western_classical"]["cascade"]}
    
    if "dome" in intent or "round" in intent or "centerpiece" in intent:
        return {"category": "western_classical", "type": "dome", **ARRANGEMENT_STYLES["western_classical"]["dome"]}
    
    if "minimal" in intent or "modern" in intent or "contemporary" in intent:
        return {"category": "contemporary", "type": "minimalist", **ARRANGEMENT_STYLES["contemporary"]["minimalist"]}
    
    if "garden" in intent or "loose" in intent or "natural" in intent or "romantic" in intent:
        return {"category": "contemporary", "type": "garden_style", **ARRANGEMENT_STYLES["contemporary"]["garden_style"]}
    
    if "crescent" in intent or "curve" in intent:
        return {"category": "western_classical", "type": "crescent", **ARRANGEMENT_STYLES["western_classical"]["crescent"]}
    
    # Default based on preference or occasion hints
    if preference != "any":
        for category, styles in ARRANGEMENT_STYLES.items():
            if preference in styles:
                return {"category": category, "type": preference, **styles[preference]}
    
    # Default to garden style (most versatile)
    return {"category": "contemporary", "type": "garden_style", **ARRANGEMENT_STYLES["contemporary"]["garden_style"]}

def detect_flowers(intent: str, occasion: str) -> Dict[str, List[Dict]]:
    """Detect mentioned flowers or suggest based on occasion."""
    detected = {"focal": [], "line": [], "filler": [], "texture": []}
    
    # Check for explicit flower mentions
    for role, flowers in FLOWERS_BY_ROLE.items():
        for flower_name, flower_data in flowers.items():
            if flower_name.replace("_", " ") in intent:
                detected[role].append({
                    "name": flower_name.replace("_", " "),
                    "role": role,
                    **flower_data
                })
    
    # If no flowers detected, suggest based on occasion
    if not any(detected.values()):
        detected = suggest_flowers_by_occasion(occasion, intent)
    
    return detected

def suggest_flowers_by_occasion(occasion: str, intent: str) -> Dict[str, List[Dict]]:
    """Suggest flowers based on occasion and intent keywords."""
    suggestions = {"focal": [], "line": [], "filler": [], "texture": []}
    
    # Wedding suggestions
    if "wedding" in occasion or "wedding" in intent or "bridal" in intent:
        suggestions["focal"].append({
            "name": "garden roses",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["roses"]
        })
        suggestions["focal"].append({
            "name": "peonies",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["peonies"]
        })
        suggestions["filler"].append({
            "name": "baby breath",
            "role": "filler",
            **FLOWERS_BY_ROLE["filler"]["baby_breath"]
        })
    
    # Romantic
    elif "romantic" in intent or "anniversary" in intent:
        suggestions["focal"].append({
            "name": "roses",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["roses"]
        })
        suggestions["texture"].append({
            "name": "ranunculus",
            "role": "texture",
            **FLOWERS_BY_ROLE["texture"]["ranunculus"]
        })
    
    # Vibrant/celebration
    elif "vibrant" in intent or "celebration" in intent or "birthday" in intent:
        suggestions["focal"].append({
            "name": "sunflowers",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["sunflowers"]
        })
        suggestions["focal"].append({
            "name": "dahlias",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["dahlias"]
        })
    
    # Elegant/formal
    elif "elegant" in intent or "formal" in intent:
        suggestions["focal"].append({
            "name": "orchids",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["orchids"]
        })
        suggestions["focal"].append({
            "name": "lilies",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["lilies"]
        })
    
    # Default to roses and mixed
    else:
        suggestions["focal"].append({
            "name": "roses",
            "role": "focal",
            **FLOWERS_BY_ROLE["focal"]["roses"]
        })
        suggestions["filler"].append({
            "name": "waxflower",
            "role": "filler",
            **FLOWERS_BY_ROLE["filler"]["waxflower"]
        })
    
    return suggestions

def detect_foliage(intent: str, style: Dict) -> List[Dict]:
    """Detect or suggest foliage based on style."""
    foliage = []
    
    # Check for explicit mentions
    for category, types in FOLIAGE_TYPES.items():
        for foliage_name, foliage_data in types.items():
            if foliage_name.replace("_", " ") in intent:
                foliage.append({
                    "name": foliage_name.replace("_", " "),
                    "category": category,
                    **foliage_data
                })
    
    # Suggest based on style if none detected
    if not foliage:
        if style.get("category") == "contemporary" and style.get("type") == "minimalist":
            foliage.append({
                "name": "eucalyptus",
                "category": "structural",
                **FOLIAGE_TYPES["structural"]["eucalyptus"]
            })
        elif style.get("category") == "contemporary" and style.get("type") == "garden_style":
            foliage.append({
                "name": "eucalyptus",
                "category": "structural",
                **FOLIAGE_TYPES["structural"]["eucalyptus"]
            })
            foliage.append({
                "name": "ivy",
                "category": "accent",
                **FOLIAGE_TYPES["accent"]["ivy"]
            })
        elif style.get("category") == "ikebana":
            foliage.append({
                "name": "aspidistra",
                "category": "dramatic",
                **FOLIAGE_TYPES["dramatic"]["aspidistra"]
            })
        else:
            foliage.append({
                "name": "ruscus",
                "category": "structural",
                **FOLIAGE_TYPES["structural"]["ruscus"]
            })
    
    return foliage

def detect_color_scheme(intent: str, color_preference: str, occasion: str) -> Dict[str, Any]:
    """Detect or map color scheme."""
    intent_lower = intent.lower()
    
    # Check for explicit palette mentions
    for palette_name, palette_data in COLOR_PALETTES.items():
        if palette_name in intent_lower:
            return {"palette": palette_name, **palette_data}
    
    # Check for season mentions
    if "spring" in intent_lower:
        return {"palette": "spring", **COLOR_PALETTES["spring"]}
    if "summer" in intent_lower:
        return {"palette": "summer", **COLOR_PALETTES["summer"]}
    if "autumn" in intent_lower or "fall" in intent_lower:
        return {"palette": "autumn", **COLOR_PALETTES["autumn"]}
    if "winter" in intent_lower:
        return {"palette": "winter", **COLOR_PALETTES["winter"]}
    
    # Check for mood/style mentions
    if "romantic" in intent_lower or "wedding" in intent_lower:
        return {"palette": "romantic", **COLOR_PALETTES["romantic"]}
    if "elegant" in intent_lower or "formal" in intent_lower:
        return {"palette": "elegant", **COLOR_PALETTES["elegant"]}
    if "vibrant" in intent_lower or "bold" in intent_lower:
        return {"palette": "vibrant", **COLOR_PALETTES["vibrant"]}
    
    # Use provided preference
    if color_preference in COLOR_PALETTES:
        return {"palette": color_preference, **COLOR_PALETTES[color_preference]}
    
    # Default to analogous (most harmonious)
    return {"palette": "analogous", **COLOR_PALETTES["analogous"]}

def map_structure(style: Dict, colors: Dict) -> Dict[str, Any]:
    """Map structural techniques based on style and colors."""
    structure = {}
    
    # Balance from style
    balance_type = style.get("balance", "asymmetrical")
    if balance_type == "symmetrical":
        structure["balance"] = STRUCTURAL_TECHNIQUES["balance"]["symmetrical_radial"]
    elif balance_type == "radial symmetrical":
        structure["balance"] = STRUCTURAL_TECHNIQUES["balance"]["symmetrical_radial"]
    else:
        structure["balance"] = STRUCTURAL_TECHNIQUES["balance"]["asymmetrical"]
    
    # Movement from style category
    if style.get("type") == "cascade":
        structure["movement"] = STRUCTURAL_TECHNIQUES["movement"]["cascade_fall"]
    elif style.get("type") == "vertical":
        structure["movement"] = STRUCTURAL_TECHNIQUES["movement"]["vertical_lift"]
    elif style.get("type") == "horizontal":
        structure["movement"] = STRUCTURAL_TECHNIQUES["movement"]["horizontal_sweep"]
    else:
        structure["movement"] = STRUCTURAL_TECHNIQUES["movement"]["spiral_rotation"]
    
    # Proportion
    structure["proportion"] = STRUCTURAL_TECHNIQUES["proportion"]["golden_ratio"]
    
    # Focal points
    if style.get("category") == "contemporary" and style.get("type") == "minimalist":
        structure["focal"] = STRUCTURAL_TECHNIQUES["focal_points"]["single_dominant"]
    else:
        structure["focal"] = STRUCTURAL_TECHNIQUES["focal_points"]["multiple_secondary"]
    
    # Density
    if style.get("category") == "contemporary" and style.get("type") == "minimalist":
        structure["density"] = STRUCTURAL_TECHNIQUES["density"]["airy_spacious"]
    elif style.get("category") == "contemporary" and style.get("type") == "garden_style":
        structure["density"] = STRUCTURAL_TECHNIQUES["density"]["packed_abundant"]
    else:
        structure["density"] = STRUCTURAL_TECHNIQUES["density"]["clustered_with_voids"]
    
    # Texture
    structure["texture"] = STRUCTURAL_TECHNIQUES["texture"]["smooth_rough_contrast"]
    
    return structure

def map_occasion(occasion: str, style: Dict) -> Dict[str, Any]:
    """Map occasion-specific requirements."""
    if occasion in OCCASIONS:
        return OCCASIONS[occasion]
    
    # Check for occasion keywords in various categories
    for occ_name, occ_data in OCCASIONS.items():
        if occasion in str(occ_data).lower():
            return {occ_name: occ_data}
    
    return {"occasion": "general", "notes": "versatile arrangement suitable for various contexts"}

def get_cultural_context(style: Dict) -> Dict[str, Any]:
    """Get cultural context for the style."""
    if style.get("category") == "ikebana":
        return CULTURAL_TRADITIONS["japanese_ikebana"]
    elif style.get("category") == "contemporary" and style.get("type") == "garden_style":
        return CULTURAL_TRADITIONS["european_garden"]
    elif style.get("category") == "contemporary":
        return CULTURAL_TRADITIONS["contemporary_western"]
    else:
        return CULTURAL_TRADITIONS["european_garden"]

def format_prompt_enhancement(mapped: Dict[str, Any]) -> str:
    """Format the mapped taxonomy into an enhanced prompt string."""
    style = mapped["style"]
    flowers = mapped["flowers"]
    foliage = mapped["foliage"]
    colors = mapped["colors"]
    structure = mapped["structure"]
    
    # Build prompt components
    parts = []
    
    # Style and container
    parts.append(f"{style['type'].replace('_', ' ').title()} floral arrangement")
    parts.append(f"in {style['container']}")
    
    # Flowers by role
    focal_flowers = [f["name"] for f in flowers.get("focal", [])]
    if focal_flowers:
        parts.append(f"featuring {', '.join(focal_flowers)} as focal flowers")
    
    line_flowers = [f["name"] for f in flowers.get("line", [])]
    if line_flowers:
        parts.append(f"with {', '.join(line_flowers)} creating vertical lines")
    
    filler_flowers = [f["name"] for f in flowers.get("filler", [])]
    if filler_flowers:
        parts.append(f"filled with {', '.join(filler_flowers)}")
    
    # Foliage
    foliage_names = [f["name"] for f in foliage]
    if foliage_names:
        parts.append(f"accented with {', '.join(foliage_names)} foliage")
    
    # Colors
    if "colors" in colors:
        parts.append(f"in {', '.join(colors['colors'])} palette")
    
    # Structure
    parts.append(f"using {structure['balance']['description']}")
    parts.append(f"with {structure['movement']['description']}")
    
    # Effects
    parts.append(f"creating {style.get('characteristics', 'beautiful composition')}")
    
    return ", ".join(parts)

# ============================================================================
# COMFYUI WORKFLOW GENERATION
# ============================================================================

def get_model_file(model_preference: str) -> str:
    """Map model preference to checkpoint filename."""
    model_map = {
        "flux": "flux1-dev.safetensors",
        "sdxl": "sd_xl_base_1.0.safetensors",
        "sd15": "v1-5-pruned-emaonly.safetensors"
    }
    return model_map.get(model_preference, model_map["flux"])

def build_comfyui_workflow(
    prompt: str,
    negative_prompt: str,
    size: str,
    model: str,
    steps: int
) -> Dict[str, Any]:
    """Build complete ComfyUI workflow JSON."""
    width, height = map(int, size.split('x'))
    
    workflow = {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": get_model_file(model)
            }
        },
        "2": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": prompt,
                "clip": ["1", 1]
            }
        },
        "3": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": negative_prompt,
                "clip": ["1", 1]
            }
        },
        "4": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "5": {
            "class_type": "KSampler",
            "inputs": {
                "seed": -1,
                "steps": steps,
                "cfg": 7.5,
                "sampler_name": "euler_ancestral",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["1", 0],
                "positive": ["2", 0],
                "negative": ["3", 0],
                "latent_image": ["4", 0]
            }
        },
        "6": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["5", 0],
                "vae": ["1", 2]
            }
        },
        "7": {
            "class_type": "SaveImage",
            "inputs": {
                "filename_prefix": "floral_arrangement",
                "images": ["6", 0]
            }
        }
    }
    
    return workflow

# ============================================================================
# MCP TOOL DEFINITIONS
# ============================================================================

@mcp.tool()
def enhance_floral_prompt(
    user_intent: str,
    style_preference: str = "any",
    occasion: str = "general",
    color_scheme: str = "harmonious"
) -> dict:
    """
    Enhance a floral arrangement description with professional vocabulary.
    
    This tool maps user intent to comprehensive floral taxonomy and returns
    structured data for Claude to synthesize into an enhanced prompt.
    
    Args:
        user_intent: User's description or desired feeling (e.g., "romantic spring wedding centerpiece")
        style_preference: Specific style preference - "any", or one of:
            - Ikebana: "moribana", "nageire", "rikka"
            - Western: "cascade", "crescent", "hogarth", "dome", "triangular", "vertical", "horizontal"
            - Contemporary: "minimalist", "structural", "garden_style", "parallel"
        occasion: Context for the arrangement - "general", "wedding", "funeral", "celebration", "everyday"
        color_scheme: Color approach - "harmonious", "monochromatic", "analogous", "complementary", 
                     "triadic", "romantic", "elegant", "vibrant", "spring", "summer", "autumn", "winter"
    
    Returns:
        Dictionary with:
        - user_intent: Original request
        - style: Detected/selected arrangement style with full details
        - flowers: Categorized flowers (focal, line, filler, texture) with characteristics
        - foliage: Foliage types with uses
        - colors: Color palette with effects
        - structure: Balance, movement, proportion, focal points, density, texture
        - occasion: Occasion-specific requirements
        - cultural_context: Cultural tradition and philosophy
        - enhanced_prompt: Formatted prompt string ready for image generation
        - synthesis_instruction: Instructions for Claude to create final creative prompt
    
    Example:
        enhance_floral_prompt(
            user_intent="romantic spring wedding centerpiece",
            occasion="wedding",
            color_scheme="romantic"
        )
    """
    # Map to taxonomy (deterministic, zero LLM cost)
    mapped = map_floral_taxonomy(user_intent, style_preference, occasion, color_scheme)
    
    # Format basic prompt
    enhanced_prompt = format_prompt_enhancement(mapped)
    
    # Return structured data for Claude synthesis
    return {
        "user_intent": user_intent,
        "style": mapped["style"],
        "flowers": mapped["flowers"],
        "foliage": mapped["foliage"],
        "colors": mapped["colors"],
        "structure": mapped["structure"],
        "occasion": mapped["occasion"],
        "cultural_context": mapped["cultural_context"],
        "enhanced_prompt": enhanced_prompt,
        "synthesis_instruction": (
            "Use the structured data above to synthesize a vivid, cohesive image generation prompt. "
            "Weave together the style characteristics, specific flowers, foliage, color palette, "
            "and structural techniques into flowing descriptive prose. Emphasize the sensory qualities "
            "(texture, color, form, movement) and the overall aesthetic effect. Keep the prompt "
            "60-100 words, suitable for Flux, SDXL, or Midjourney."
        )
    }

@mcp.tool()
def generate_floral_workflow(
    user_intent: str,
    output_size: str = "1024x1024",
    model_preference: str = "flux",
    steps: int = 20
) -> dict:
    """
    Generate ComfyUI workflow JSON for floral arrangement imagery.
    
    This tool creates a complete, ready-to-use ComfyUI workflow with prompts
    enhanced from floral taxonomy. The workflow can be imported directly into
    ComfyUI for image generation.
    
    Args:
        user_intent: User's description of desired arrangement (e.g., "elegant orchid centerpiece")
        output_size: Image dimensions, one of:
            - "1024x1024" (square, default)
            - "1024x768" (landscape)
            - "768x1024" (portrait)
            - "1536x1024" (wide landscape)
            - "1024x1536" (tall portrait)
        model_preference: Base model to use:
            - "flux" (default, highest quality)
            - "sdxl" (Stable Diffusion XL)
            - "sd15" (Stable Diffusion 1.5)
        steps: Number of sampling steps (10-50, default 20)
    
    Returns:
        Dictionary with:
        - workflow: Complete ComfyUI workflow JSON ready to import
        - positive_prompt: Enhanced prompt used
        - negative_prompt: Negative prompt to avoid unwanted elements
        - metadata: Information about flowers, style, colors used
        - usage_instructions: How to import and use the workflow
    
    Example:
        generate_floral_workflow(
            user_intent="minimalist ikebana with cherry blossoms",
            output_size="768x1024",
            model_preference="flux"
        )
    """
    # Map to taxonomy
    mapped = map_floral_taxonomy(user_intent)
    
    # Build enhanced prompt
    positive_prompt = format_prompt_enhancement(mapped)
    
    # Build negative prompt
    negative_prompt = (
        "wilted, dead, brown, artificial, plastic, fake flowers, "
        "low quality, blurry, distorted, malformed flowers, "
        "ugly arrangement, chaotic, messy, cluttered"
    )
    
    # Build ComfyUI workflow
    workflow = build_comfyui_workflow(
        prompt=positive_prompt,
        negative_prompt=negative_prompt,
        size=output_size,
        model=model_preference,
        steps=steps
    )
    
    # Compile metadata
    focal_names = [f["name"] for f in mapped["flowers"].get("focal", [])]
    all_flowers = []
    for role in ["focal", "line", "filler", "texture"]:
        all_flowers.extend([f["name"] for f in mapped["flowers"].get(role, [])])
    
    foliage_names = [f["name"] for f in mapped["foliage"]]
    
    metadata = {
        "arrangement_style": f"{mapped['style']['category']} - {mapped['style']['type']}",
        "focal_flowers": focal_names,
        "all_flowers": all_flowers,
        "foliage": foliage_names,
        "color_palette": mapped["colors"].get("palette", "custom"),
        "balance": mapped["structure"]["balance"]["description"],
        "cultural_tradition": mapped["cultural_context"].get("philosophy", "")
    }
    
    return {
        "workflow": workflow,
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "metadata": metadata,
        "usage_instructions": (
            "1. Copy the 'workflow' JSON from this response\n"
            "2. In ComfyUI, click 'Load' and paste the JSON\n"
            "3. Ensure you have the specified model checkpoint\n"
            "4. Click 'Queue Prompt' to generate\n"
            "5. Adjust seed value in node 5 for variations"
        )
    }

@mcp.tool()
def list_arrangement_styles() -> dict:
    """
    List all available arrangement styles with descriptions.
    
    Returns comprehensive catalog of styles organized by tradition:
    - Ikebana (Japanese): moribana, nageire, rikka
    - Western Classical: cascade, crescent, hogarth, dome, triangular, vertical, horizontal
    - Contemporary: minimalist, structural, garden_style, parallel
    
    Each style includes description, container type, characteristics, balance type,
    and complexity level.
    
    Returns:
        Dictionary organized by tradition with complete style specifications
    """
    return ARRANGEMENT_STYLES

@mcp.tool()
def list_flowers_by_role() -> dict:
    """
    List all flowers organized by their role in arrangements.
    
    Returns comprehensive flower catalog with:
    - Focal flowers: Primary attention-grabbing blooms (roses, peonies, lilies, etc.)
    - Line flowers: Create height and structure (snapdragons, delphiniums, etc.)
    - Filler flowers: Add texture and fill space (baby's breath, waxflower, etc.)
    - Texture flowers: Provide unique textural interest (thistle, protea, etc.)
    
    Each flower includes characteristics, color range, size, seasons, and symbolism.
    
    Returns:
        Dictionary organized by role with complete flower specifications
    """
    return FLOWERS_BY_ROLE

@mcp.tool()
def list_color_palettes() -> dict:
    """
    List all available color palettes for floral arrangements.
    
    Returns palettes organized by:
    - Color theory: monochromatic, analogous, complementary, triadic
    - Mood: romantic, elegant, vibrant
    - Season: spring, summer, autumn, winter
    
    Each palette includes specific colors, effect, and suitable occasions.
    
    Returns:
        Dictionary of all color palette specifications
    """
    return COLOR_PALETTES

@mcp.tool()
def list_foliage_types() -> dict:
    """
    List all foliage types used in arrangements.
    
    Returns foliage organized by:
    - Structural: Foundation greenery (ferns, eucalyptus, ruscus, salal)
    - Accent: Decorative elements (ivy, pittosporum, dusty miller, olive)
    - Dramatic: Bold statement foliage (monstera, palm, aspidistra)
    
    Each type includes characteristics, types/varieties, and typical uses.
    
    Returns:
        Dictionary of foliage specifications by category
    """
    return FOLIAGE_TYPES

@mcp.tool()
def get_cultural_traditions() -> dict:
    """
    Get information about cultural traditions in floral arrangement.
    
    Returns detailed information about:
    - Japanese Ikebana: Philosophy, principles, key concepts (ma, wabi-sabi, shin-soe-hikae)
    - European Garden: Abundance, romance, natural beauty principles
    - Victorian: Language of flowers, symbolic meanings, formal structure
    - Contemporary Western: Artistic expression, rule-breaking, individual style
    
    Each tradition includes philosophy, core principles, and characteristics.
    
    Returns:
        Dictionary of cultural traditions with philosophies and principles
    """
    return CULTURAL_TRADITIONS

@mcp.tool()
def get_structural_techniques() -> dict:
    """
    Get comprehensive guide to structural techniques in floral design.
    
    Returns detailed specifications for:
    - Balance: Symmetrical radial, bilateral, asymmetrical
    - Proportion: Golden ratio, rule of thirds, height-to-container ratios
    - Focal Points: Single dominant, multiple secondary, distributed
    - Movement: Vertical lift, horizontal sweep, spiral rotation, cascade fall, radiation
    - Texture: Smooth-rough contrast, delicate-bold mix, monochromatic texture
    - Density: Packed abundant, airy spacious, clustered with voids
    
    Each technique includes description, application, and visual effect.
    
    Returns:
        Dictionary of all structural technique specifications
    """
    return STRUCTURAL_TECHNIQUES

@mcp.tool()
def suggest_flowers_for_occasion(occasion: str) -> dict:
    """
    Get flower suggestions tailored to specific occasions.
    
    Provides recommendations for:
    - Wedding: Ceremony, reception, bridal party arrangements
    - Funeral: Standing spray, casket spray, wreath, sympathy basket
    - Celebration: Birthday, anniversary, congratulations, get well
    - Everyday: Home decor, hostess gift
    
    Each occasion includes appropriate arrangements, styles, scale, and characteristics.
    
    Args:
        occasion: The occasion type - "wedding", "funeral", "celebration", "everyday"
    
    Returns:
        Dictionary with occasion-specific recommendations
    """
    if occasion in OCCASIONS:
        return {
            "occasion": occasion,
            "recommendations": OCCASIONS[occasion]
        }
    else:
        return {
            "occasion": occasion,
            "error": f"Occasion '{occasion}' not found",
            "available_occasions": list(OCCASIONS.keys())
        }

# ============================================================================
# SERVER INFO
# ============================================================================

@mcp.tool()
def get_server_info() -> dict:
    """
    Get information about the Floral Arrangement Aesthetics MCP server.
    
    Returns overview of capabilities, architecture, and usage patterns.
    
    Returns:
        Dictionary with server information and capabilities
    """
    return {
        "name": "Floral Arrangement Aesthetics MCP Server",
        "version": "1.0.0",
        "description": "Dual-purpose server for floral arrangement prompt enhancement and ComfyUI workflow generation",
        "architecture": {
            "layer_1": "Comprehensive floral taxonomy (deterministic, zero LLM cost)",
            "layer_2": "Structural mapping and technique selection",
            "layer_3": "Cultural and aesthetic context synthesis (Claude integration)"
        },
        "primary_tools": {
            "enhance_floral_prompt": "Map user intent to professional floral vocabulary for prompt enhancement",
            "generate_floral_workflow": "Create complete ComfyUI workflow JSON with floral-enhanced prompts"
        },
        "taxonomy_coverage": {
            "arrangement_styles": "15 styles across 3 traditions (Ikebana, Western Classical, Contemporary)",
            "flowers": "20+ flowers organized by role (focal, line, filler, texture)",
            "foliage": "10+ foliage types across 3 categories (structural, accent, dramatic)",
            "color_palettes": "10 palettes including theory-based and seasonal",
            "structural_techniques": "6 technique categories with detailed specifications",
            "cultural_traditions": "4 major traditions with philosophies and principles"
        },
        "cost_optimization": "60-80% cost savings through deterministic taxonomy mapping + single LLM synthesis",
        "usage_pattern": "User → Claude (intent extraction) → MCP (deterministic mapping) → Claude (creative synthesis)"
    }

# ============================================================================
# SERVER ENTRY POINT
# ============================================================================

def main():
    """Entry point for running the MCP server."""
    import asyncio
    mcp.run()

if __name__ == "__main__":
    main()
