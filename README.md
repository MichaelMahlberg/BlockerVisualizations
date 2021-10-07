# Blocker Clustering Treemap    

Visualize blockers by impact during [blocker clustering \[1\]](#ref-1).

![Screenshot](doc/screenshot.png)

## GDPR

Note that the `data` directory is excluded from version control for GDPR reasons by means of a `.gitignore` file. This folder is expected to contain the input data.

## Prerequisites

Install the dependencies listed in `requirements.txt`:

```shell
pip install -r requirements.txt
```

## Execute: Visualize Blockers in a Treemap

1. Export your data to `./data/BlockersPrepared.csv`
2. `python3 plotly-blocker-treemap.py data/BlcokersPrepared.csv`

## References

<a name="ref-1">[1]</a> kanbanize.com: [Blocker Clustering](https://kanbanize.com/kanban-resources/kanban-analytics/block-clustering)
