# Workflow: Generate and Apply Color Palette

<required_reading>
**Read this reference file NOW:**
1. references/color-theory-guide.md
</required_reading>

<process>

## Step 1: Research Project Context

**Search the codebase for project description:**
```bash
# Look for README, package.json description, or about pages
cat README.md 2>/dev/null || echo "No README found"
grep -A2 '"description"' package.json 2>/dev/null
```

**Identify key information:**
- What does this application do?
- What industry/domain? (fintech, healthcare, e-commerce, social, productivity, etc.)
- Who is the target audience? (enterprise, consumers, developers, specific demographics)
- What is the desired emotional response? (trust, excitement, calm, innovation)

## Step 2: Locate Theme Configuration

**Search for existing theme/color definitions:**
```bash
# CSS variables
grep -rn "--primary\|--background\|--accent\|--foreground" --include="*.css" .

# Theme objects (JS/TS)
grep -rn "createTheme\|extendTheme\|palette:\|colors:" --include="*.ts" --include="*.tsx" --include="*.js" .

# Tailwind config
grep -rn "theme:\|extend:" tailwind.config.* 2>/dev/null
```

**Document findings:**
- Framework detected: [Tailwind/shadcn | Material UI | Chakra | Plain CSS | Other]
- Theme file location: [path/to/file]
- Variable format: [HSL | HEX | RGB | Token-based]
- Existing brand colors to preserve: [list or none]

## Step 3: Gather Missing Information

**If any of these are unclear, ASK THE USER:**

1. **App purpose/industry** (if not found in README):
   > "I couldn't determine the app's primary purpose. What industry is this for? (e.g., fintech, healthcare, e-commerce, social, productivity)"

2. **Target audience** (if not obvious):
   > "Who is the primary user? (e.g., enterprise professionals, general consumers, developers, specific age group)"

3. **Existing brand colors** (if uncertain):
   > "Are there any existing brand colors that must be preserved? If so, please provide them."

4. **Color preference direction** (optional enhancement):
   > "Any preference for warm vs. cool tones, or specific colors to avoid?"

**If context is sufficient, proceed without asking.**

## Step 4: Select Primary Color

**Based on gathered context, select primary color using psychological mapping:**

| Industry/Purpose | Recommended Primary | Psychological Rationale |
|------------------|---------------------|-------------------------|
| Finance/Banking | Blue (#2563eb) | Trust, security, reliability |
| Healthcare/Wellness | Teal/Green (#0d9488) | Health, calm, growth |
| E-commerce | Blue or Orange (#f97316) | Trust or urgency/excitement |
| Social/Community | Purple or Pink (#8b5cf6) | Creativity, connection |
| Productivity/SaaS | Blue or Indigo (#4f46e5) | Focus, professionalism |
| AI/Innovation | Purple/Violet (#7c3aed) | Sophistication, innovation |
| Eco/Sustainability | Green (#16a34a) | Nature, growth, responsibility |
| Food/Restaurant | Red or Orange (#dc2626) | Appetite, warmth, energy |
| Premium/Luxury | Deep Purple or Gold (#7c2d12) | Sophistication, exclusivity |

**Generate tonal scale for primary:**
- 50: Lightest tint (backgrounds)
- 100-400: Progressively darker tints
- 500: Base primary color
- 600-900: Progressively darker shades

## Step 5: Build Complete Palette

**Generate these color categories:**

### Primary Scale (10 steps)
Based on selected hero color, create 50-900 scale.

### Secondary Color
- Option A: Analogous to primary (harmonious, subtle)
- Option B: Complementary to primary (vibrant, high-contrast accents)

### Neutral Scale (Tinted Grays)
- NOT pure gray—tint with primary hue at ~5-10% saturation
- Creates cohesion with brand palette
- Scale: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950

### Semantic Colors
```
Success: Green    → #16a34a (base), #15803d (dark variant)
Warning: Amber    → #d97706 (base), #b45309 (dark variant)  
Error: Red        → #dc2626 (base), #b91c1c (dark variant)
Info: Blue        → #0284c7 (base), #0369a1 (dark variant)
```

### Surface Colors
- Background (light): Near-white with slight warm/cool tint
- Background (dark): Deep gray/charcoal, NOT pure black (#09090b works well)
- Cards/Elevated surfaces: Slightly lighter than background in dark mode

## Step 6: Validate Accessibility

**Check these critical pairings (must be ≥4.5:1):**
- [ ] Primary on background
- [ ] Foreground text on background
- [ ] Foreground text on primary (primary-foreground)
- [ ] Foreground text on secondary
- [ ] Error text readable on background
- [ ] Muted text on background (≥4.5:1 for body, ≥3:1 for large)

**Check UI component contrast (must be ≥3:1):**
- [ ] Border color against background
- [ ] Focus ring against background
- [ ] Input borders against background

**Tools for validation:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Use OKLCH for generating perceptually uniform scales

## Step 7: Generate Dark Mode Variants

**Dark mode is NOT inversion. Apply these transformations:**

1. **Background**: Deep charcoal (e.g., `222.2 84% 4.9%` in HSL)
2. **Foreground**: Light neutral (e.g., `210 40% 98%`)
3. **Primary**: May need slight lightening for visibility
4. **Reduce saturation**: ~10-20% reduction prevents eye strain
5. **Elevation mapping**: Higher surfaces = lighter shades
6. **Re-validate all contrast ratios**

## Step 8: Apply to Theme Configuration

**Based on framework detected in Step 2:**

### For Tailwind/shadcn (globals.css):
```css
@layer base {
  :root {
    --background: [H] [S]% [L]%;
    --foreground: [H] [S]% [L]%;
    --card: [H] [S]% [L]%;
    --card-foreground: [H] [S]% [L]%;
    --popover: [H] [S]% [L]%;
    --popover-foreground: [H] [S]% [L]%;
    --primary: [H] [S]% [L]%;
    --primary-foreground: [H] [S]% [L]%;
    --secondary: [H] [S]% [L]%;
    --secondary-foreground: [H] [S]% [L]%;
    --muted: [H] [S]% [L]%;
    --muted-foreground: [H] [S]% [L]%;
    --accent: [H] [S]% [L]%;
    --accent-foreground: [H] [S]% [L]%;
    --destructive: [H] [S]% [L]%;
    --destructive-foreground: [H] [S]% [L]%;
    --border: [H] [S]% [L]%;
    --input: [H] [S]% [L]%;
    --ring: [H] [S]% [L]%;
    --radius: 0.5rem;
  }

  .dark {
    --background: [dark values];
    /* ... all dark mode values */
  }
}
```

### For Material UI (theme.ts):
```typescript
import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    primary: { main: '#[hex]', light: '#[hex]', dark: '#[hex]' },
    secondary: { main: '#[hex]' },
    error: { main: '#[hex]' },
    warning: { main: '#[hex]' },
    info: { main: '#[hex]' },
    success: { main: '#[hex]' },
    background: { default: '#[hex]', paper: '#[hex]' },
  },
});
```

### For Plain CSS:
```css
:root {
  --color-primary-50: #[hex];
  --color-primary-100: #[hex];
  /* ... full scale */
  --color-primary-900: #[hex];
  
  --color-neutral-50: #[hex];
  /* ... */
}

@media (prefers-color-scheme: dark) {
  :root {
    /* dark mode overrides */
  }
}
```

## Step 9: Present Summary to User

**After applying colors, summarize:**

```
## Color Palette Applied

**Primary**: [color name] (#hex) - [psychological rationale]
**Secondary**: [color name] (#hex) - [relationship to primary]
**Accent**: [color name] (#hex) - [purpose]

**Neutrals**: [warm/cool tinted] grays based on primary hue

**Semantic Colors**:
- Success: #hex
- Warning: #hex  
- Error: #hex
- Info: #hex

**Applied to**: [file path]

**Accessibility**: All primary text combinations meet WCAG AA (4.5:1+)

**Next steps**: 
- Review the changes visually in browser
- Test with color blindness simulator
- Adjust if any combinations feel off
```

</process>

<success_criteria>
This workflow is complete when:
- [ ] Project purpose and audience identified (from codebase or user input)
- [ ] Theme file location discovered
- [ ] Primary color selected with documented rationale
- [ ] Full palette generated (primary, secondary, neutrals, semantics)
- [ ] Light and dark mode variants created
- [ ] Accessibility validated (4.5:1 for text, 3:1 for UI)
- [ ] Colors applied to correct configuration file
- [ ] Summary presented to user
</success_criteria>
