# CropPilot – Command-Line Farm Planner

**Author:** Ramandeep Singh  
**Date:** April 2025 *(Last Updated April 2025)*  
**Language:** Python  

---

## Status: In Development (Phase 1)  
## License: MIT  

---

## How to Run the Program

**Python:** Python 3.x  
**Libraries:** N/A  

```bash
python _main.py
```

---

## Project Overview

CropPilot is a Python-based, open-source tool that helps small-scale farmers, gardeners, and hobbyists plan, track, and analyze their crop operations.

This tool is designed to be lightweight, extensible, and practical, providing users with clear insights into profitability, sustainability, and resource management without needing enterprise tools.

This project started as a way to apply computer science to agriculture, which is one of the many fields I am interested in applying my major to. It is built to grow alongside my learning.

---

## Target Users

- Small-scale farmers looking for a simple digital record-keeping solution  
- Market gardeners who sell locally and track yields, costs, pricing  
- Students studying agriculture, sustainability, or agri-finance  

---

## Development Phases & Roadmap

### Phase 1 – CLI (Completed)
**Goal:** Build a working command-line interface that lets users input, view, and save crop data.  
**Features:**
- Add crop with name, cost, yield, and price  
- Remove crop by number  
- Calculate profit (revenue - cost)  
- Save/load from `crops.json`  
- Auto-save on exit  
- View all crops  
- CLI Menu  

---

### Phase 2 – Data Integration (In Progress)
**Goal:** Introduce static, realistic data to enrich crop records and enhance user experience.  
**Features:**
- Use 2-month static average crop prices (editable)  
- Search/filter by crop name  
- Group crops by category  
- Summary dashboard (total profit, cost, revenue)  
- Currency toggle and conversion (USD ↔ CAD using static rates)  
- Export to CSV  

---

### Phase 3 – Visualization (Not Started)
**Goal:** Make data insights and trends visual while retaining CLI.  
**Features:**
- ASCII bar charts (profit per crop)  
- Top 3 most profitable crops  
- Enhanced CLI readability  
- Summary analytics (averages, min, max)  

---

### Phase 4 – Sustainability (Not Started)
**Goal:** Let users track environmental impact of farming practices.  
**Features:**
- Carbon footprint calculator  
- Fertilizer, irrigation, and tillage score system  
- Carbon ratings (low, medium, high)  
- Sustainability score  

---

### Phase 5 – GUI or Web App (Concept)
**Goal:** Build a simple interface for non-technical users.  
**GUI Features:**
- Button-based layout  
- Form-based data entry  
- Live feedback on profit and scores  

**Web Features:**
- Web-hosted form  
- Graphical dashboard  

---

## Notes

- This roadmap will evolve over time as the project develops  
- Each phase builds on the last while maintaining a CLI (Excluding Phase 5)

---
