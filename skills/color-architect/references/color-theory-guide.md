<color_science>

**Digital Color Models**

Web applications use RGB additive color (light-based, not pigment). Maximum RGB = white.

| Color Space | Perceptual Accuracy | Use Case |
|-------------|---------------------|----------|
| RGB/HEX | Low (technical) | Final code output |
| HSL | Medium (mathematical) | Basic adjustments—flawed for perceived luminance |
| LCH/OKLCH | High (perceptual) | Building accessible, consistent scales |
| HCT | High (algorithmic) | Material Design 3 dynamic theming |

**Why HSL Fails**: HSL calculates lightness mathematically, not perceptually. A blue and yellow with identical HSL lightness appear vastly different to human eyes—yellow looks much brighter. This causes accessibility failures.

**Preferred: OKLCH or HCT** for generating tonal scales where colors maintain consistent visual weight across hues.

</color_science>

<harmonic_relationships>

**Color Wheel Geometry**

- **Monochromatic**: Single hue, varying tints/shades. Premium minimalist brands. Low cognitive load.
- **Analogous**: Adjacent colors (e.g., blue → blue-green → green). Calming, cohesive. Good for backgrounds.
- **Complementary**: Opposite colors (e.g., orange/blue). Maximum contrast. Reserve for primary CTAs.
- **Triadic**: Three evenly-spaced colors. Vibrant but requires one dominant color to avoid visual strain.
- **Split-complementary**: One base + two colors adjacent to its complement. High contrast with less tension.

</harmonic_relationships>

<psychological_mapping>

**Emotional Impact by Hue**

| Hue | Psychology | Industry Standard | Example Use |
|-----|------------|-------------------|-------------|
| Blue | Trust, security, calm, reliability | Fintech, SaaS, Healthcare | Banking dashboards, login screens |
| Red | Urgency, passion, energy, danger | E-commerce, Food, Alerts | "Limited Time" offers, error messages |
| Green | Prosperity, growth, health, nature | Wellness, Finance, Eco-tech | Success notifications, sustainability apps |
| Yellow | Optimism, happiness, creativity | Youth, Promotional, Innovation | Creative tools, promotional highlights |
| Purple | Luxury, mystery, sophistication | Premium Tech, AI, Creativity | High-end subscription tiers |
| Orange | Warmth, excitement, friendliness | Travel, Fitness, Creative | Activity trackers, social apps |

**Cultural Considerations**:
- White = purity (Western) but mourning (parts of Asia)
- Green = positive stock trend (Western) but red = positive (Chinese markets)
- Always research target regional markets

</psychological_mapping>

<trends_2025>

**Current Design Direction**

The hyper-saturated neon "tech" aesthetic is fading. 2025 favors:

- **Mocha Mousse / Grounded Neutrals**: Warm browns, soft beiges as primary backgrounds. Creates "space to breathe."
- **Digital Lavender / Solace Blue**: Soft tech hues for healthcare/wellness. Communicate serenity.
- **Hyper-Natural Greens**: Moss, sage, algae tones for ecological authenticity.
- **Retro-Futurism**: 1970s-80s revival (mustard yellows, coral pinks) for Gen Z nostalgia.

**Key Shift**: From cold minimalism to emotionally warm, tactile digital spaces.

</trends_2025>

<distribution_framework>

**The 60-30-10 Rule**

| Percentage | Role | Application | Goal |
|------------|------|-------------|------|
| 60% | Dominant | Backgrounds, large sections | Set mood, reduce cognitive load |
| 30% | Secondary | Sidebars, navigation, cards | Structure and brand support |
| 10% | Accent | CTAs, icons, active states | Highlight critical actions |

**Implementation**:
- 60% is often a neutral (white, soft gray, deep charcoal)
- If design feels cluttered, swap dominant/secondary
- Layer surfaces for depth (glassmorphism, elevation)

**Dark Mode Layering**:
- Surfaces become lighter as they "lift" toward user
- Base Gray 100 → component Gray 90 (component appears closer)

</distribution_framework>

<accessibility_requirements>

**WCAG 2.1 AA Standards**

| Standard | Text Type | Required Ratio |
|----------|-----------|----------------|
| WCAG AA | Normal text (<18pt) | 4.5:1 |
| WCAG AA | Large text (>18pt) | 3:1 |
| WCAG AAA | Normal text | 7:1 (government, healthcare) |
| WCAG 2.1 | UI Components (borders, focus rings) | 3:1 |

**Critical Rules**:
- Never rely on color alone (add icons, text labels for states)
- Test with color blindness simulators (protanopia, deuteranopia, tritanopia)
- Error states: red + error icon + descriptive text
- Environmental testing: colors appear different in bright vs. dark rooms

**Dark Mode Specifics**:
- Reduce saturation to prevent "vibrating" colors
- Re-test all contrast ratios (don't assume they transfer)
- Consider True Tone/white point adaptivity on modern displays

</accessibility_requirements>

<token_architecture>

**Design Token Tiers**

| Tier | Example | Purpose |
|------|---------|---------|
| Reference (Primitive) | `color.blue.500` | Raw values—the source palette |
| System (Semantic) | `color.primary`, `color.on-surface` | Purpose-based, theme-aware |
| Component | `button.primary.background` | Element-specific overrides |

**"On" Color Logic**:
Every surface color needs a corresponding "on" color for content:
- `primary` → `on-primary`
- `surface` → `on-surface`
- `error` → `on-error`

These pairs are designed to meet contrast requirements automatically.

**Semantic Roles**:
| Token Role | Function | Example Component |
|------------|----------|-------------------|
| Primary | High-emphasis actions | FAB, primary buttons |
| Secondary | Less prominent actions | Filter chips, nav icons |
| Tertiary | Contrasting accents | Badges, input highlights |
| Error | Critical issues | Error messages, destructive buttons |
| Surface | Background foundations | Page backgrounds, cards |

</token_architecture>

<generation_process>

**Step-by-Step Color Selection**

1. **Define Personality**: What emotional response is needed? (trustworthy, energetic, calm, innovative)

2. **Select Primary**: Choose hero color aligned with industry/emotion. Use as Base-500.

3. **Generate Tonal Scale**: Create tints (100-400) and shades (600-900):
   - Use OKLCH/LCH for perceptual uniformity
   - Adjust lightness in ~10% steps
   - Keep hue constant, reduce saturation slightly at extremes

4. **Build Neutral Foundation**: 
   - Avoid pure gray (#888)
   - Tint neutrals with primary hue (adds "liveliness")
   - Luminance difference of ~50 steps ≈ 4.5:1 contrast

5. **Map Semantic Colors**:
   - Success: Green (confirm, complete)
   - Warning: Yellow/Amber (caution, attention)
   - Error: Red (failure, destructive)
   - Info: Blue (neutral information)

6. **Define Interactive States**:
   - Hover: Half-step lighter/darker than base
   - Active/Pressed: Two full steps deeper/lighter
   - Disabled: Desaturated, low-contrast gray
   - Focus: High-visibility ring (often accent color)

7. **Create Dark Mode Variants**:
   - Don't invert—redesign for dark backgrounds
   - Reduce saturation 10-20%
   - Use lighter surfaces for elevation
   - Flip stroke/border logic (lighter on dark)

8. **Validate**: Check every combination with contrast checker

</generation_process>

<css_variable_patterns>

**Tailwind/shadcn Pattern (HSL)**
```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --border: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  /* ... dark variants */
}
```

**Standard CSS Variables (HEX)**
```css
:root {
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-500: #3b82f6;
  --color-primary-900: #1e3a8a;
}
```

**Material UI Pattern**
```typescript
const theme = createTheme({
  palette: {
    primary: { main: '#1976d2' },
    secondary: { main: '#dc004e' },
  },
});
```

</css_variable_patterns>

<framework_detection>

**Identifying Theme Location**

Search patterns for common frameworks:

| Framework | Search Pattern | Typical Location |
|-----------|---------------|------------------|
| Tailwind/shadcn | `--background:`, `--primary:` | `globals.css`, `index.css` |
| Material UI | `createTheme`, `palette:` | `theme.ts`, `theme/index.ts` |
| Chakra UI | `extendTheme`, `colors:` | `theme.ts`, `theme/index.ts` |
| Styled Components | `ThemeProvider`, `theme =` | `theme.ts`, `styles/theme.ts` |
| CSS Modules | `:root {`, `--color-` | `variables.css`, `globals.css` |
| Ant Design | `ConfigProvider`, `token:` | `theme.ts`, `config/theme.ts` |

**Search commands**:
```bash
# Find CSS variable definitions
grep -r "--primary\|--background\|--accent" --include="*.css"

# Find theme objects
grep -r "createTheme\|extendTheme\|ThemeProvider" --include="*.ts" --include="*.tsx"

# Find color configurations
grep -r "palette:\|colors:\|colorScheme:" --include="*.ts" --include="*.tsx"
```

</framework_detection>
