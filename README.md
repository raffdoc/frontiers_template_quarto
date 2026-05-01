# Quarto Frontiers Template

A Quarto custom format extension targeting the official [Frontiers Journal Author Guidelines](https://www.frontiersin.org/guidelines/author-guidelines). 

## Installation

To install this template into your Quarto project, run the following command within your project directory:

```bash
quarto add raffdoc/frontiers_template_quarto
```

## Sub-Journals Option

You can specify a distinct Frontiers sub-journal which correctly updates the running headers of the final PDF:
```yaml
format:
  frontiers-pdf:
    journal: "Frontiers in Cardiovascular Medicine"
```
You can consult the official [Frontiers Journals List](https://www.frontiersin.org/journals) online to find the exact name of the target sub-journal.

## Custom Sub-Journal Logos

If your specific sub-journal requires a customized logo graphic (such as "Frontiers in Cardiovascular Medicine"), you can override the default Frontiers placeholder image using the `logo:` YAML property. 

```yaml
format:
  frontiers-pdf:
    logo: "pics/cardiovascular_medicine.eps"
```

A copy of the standard Frontiers logo has been securely provided inside the `pics/` directory as a starter placeholder template.

## Usage

This extension provides the `frontiers-pdf` format which builds against the official LaTeX class files provided by the journal.

To render the example template, use the following Quarto command:
```bash
quarto render template.qmd
```

## Structure
- `template.qmd`: An example Quarto document showcasing Frontiers YAML structure, headers, and standard contents.
- `test.bib`: A BibTeX file used to generate references.
- `_extensions/frontiers/`: The directory containing the extension configuration (`_extension.yml`), partials (`title.tex`, `before-body.tex`), and required LaTeX assets (class files, bibliography styles, and logos).
