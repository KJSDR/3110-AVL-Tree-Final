# Recipe AVL Tree

A self-balancing binary search tree (AVL) for searching and browsing recipes. Built as a final project for ACS 3310 to explore how tree structures can improve search performance over naive linear lookups.

## Dataset

Uses two recipe datasets from [Epicurious](https://www.epicurious.com/) and [Food Network](https://www.foodnetwork.com/) (about 34k recipes total).

## Features

- Search recipes by exact title in O(log n)
- Prefix search (autocomplete-style)
- Browse all recipes in alphabetical order
- Tree stays balanced on insertion via AVL rotations

## Setup

```bash
git clone <your-repo-url>
cd recipe-avl-tree
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Running Tests

```bash
pip install pytest
python -m pytest tests/
```

## Project Structure

```
src/
    __init__.py
    avl_node.py       # Node class
    avl_tree.py       # AVL tree implementation
    recipe_store.py   # Data loading and tree population
main.py             # CLI entry point
tests/              # Unit tests
    __init__.py
    test_avl_tree.py
data/               # Recipe JSON files
    recipes_raw_nosource_epi.json
    recipes_raw_nosource_fn.json
```