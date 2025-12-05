#  Artificial Intelligence

This repository contains exercises from the **AI (Artificial Intelligence)** class — covering topics such as Python basics, data analytics, agents, and more.

Further theory explanations and algorithm descriptions can be found [in this Notion page](https://kaiane.notion.site/Artificial-Intelligence-274c701cca24800385c6c9aaf657dcc7?source=copy_link).

---

##  Setup

Each folder contains its **own virtual environment** (`.venv`) created with:

```bash
python -m venv venv
```

Before running any notebook or script, make sure to activate it:

```bash
 .\venv\Scripts\activate
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

P.S: Naming the kernel:

```bash
pip install jupyter ipykernel
```

```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```
The venv will be available at the Jupyter Environment Sessions.

Freezing the dependencies:

```bash
pip freeze > requirements.txt
```

---

##  Structure

* `01_python_basics/` — Intro to Python syntax and logic
* `02_data_analytics/` — Working with data and visualizations
* `03_data_analytics/` — Libs and tools for data manipulation
* `04_agents/` — AI agents and simple simulations

---

## 💡 Notes

* Always activate the correct `.venv` before running the notebooks.
* You can create new environments independently for each module if needed.
* Make sure your VS Code kernel points to the right interpreter.

To deactivate the venv:

```bash
deactivate
```
---
