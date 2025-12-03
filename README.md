# Floral Arrangement Aesthetics MCP Server

Dual-purpose MCP server providing professional floral arrangement vocabulary for:
1. **Prompt Enhancement** - Enrich image generation prompts with floral design terminology
2. **ComfyUI Workflow Generation** - Create complete workflows with floral-enhanced prompts

## Architecture

**Three-Layer Design** (60-80% cost optimization):
- **Layer 1**: Comprehensive floral taxonomy (deterministic, zero LLM cost)
- **Layer 2**: Structural mapping and technique selection
- **Layer 3**: Creative synthesis (single Claude call)

## Taxonomy Coverage

- **15 Arrangement Styles** across 3 traditions (Ikebana, Western Classical, Contemporary)
- **20+ Flowers** organized by role (focal, line, filler, texture)
- **10+ Foliage Types** across 3 categories (structural, accent, dramatic)
- **10 Color Palettes** including theory-based and seasonal
- **6 Structural Technique Categories** with detailed specifications
- **4 Cultural Traditions** with philosophies and principles

## Installation

```bash
# Clone or extract the project
cd floral-arrangement-mcp

# Install in development mode
pip install -e ".[dev]"

# Run tests
./tests/run_tests.sh
```

## Usage with Claude Desktop

Add to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "floral-arrangement-aesthetics": {
      "command": "python",
      "args": ["-m", "floral_arrangement_mcp.server"]
    }
  }
}
```

## Available Tools

### Primary Tools

- **enhance_floral_prompt** - Map user intent to professional floral vocabulary
- **generate_floral_workflow** - Create complete ComfyUI workflow JSON

### Reference Tools

- **list_arrangement_styles** - Get all 15 arrangement styles
- **list_flowers_by_role** - Get flowers organized by role
- **list_color_palettes** - Get all color palette options
- **list_foliage_types** - Get all foliage types
- **get_cultural_traditions** - Get cultural tradition details
- **get_structural_techniques** - Get structural technique specifications
- **suggest_flowers_for_occasion** - Get occasion-specific recommendations
- **get_server_info** - Get server capabilities overview

## Quick Examples

### Enhance a Simple Description
```
User: "romantic spring wedding centerpiece"
Returns: Professional floral vocabulary with style, flowers, colors, structure
```

### Generate ComfyUI Workflow
```
User: "minimalist ikebana arrangement"
Returns: Complete workflow JSON ready to import into ComfyUI
```

## Documentation

- `docs/USAGE_EXAMPLES.md` - 18 detailed usage scenarios
- `docs/QUICK_REFERENCE.md` - Printable taxonomy reference
- `docs/DEPLOYMENT.md` - Deployment instructions

## Development

```bash
# Run tests
pytest tests/

# Format code
black src/ tests/

# Lint
ruff check src/ tests/
```

## License

MIT License
