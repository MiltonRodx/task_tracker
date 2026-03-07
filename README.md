# Task Tracker (Python CLI)

A simple **Python command-line task tracker** built as a beginner backend project.  
It stores tasks in a local `userdata.json` file and allows basic task management from the terminal.
https://github.com/MiltonRodx/task_tracker
---

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as **done** or **in-progress**
- List all tasks or filter by status
- Automatic task ID generation
- Creation and update timestamps

---

## Requirements

- Python 3.8+
- No external dependencies

---

## Run

```bash
python app.py <command> [arguments]
```

## Commands

### Add a task
```bash
python app.py add "Task description"
```

The program will ask for a status:

```
done(1) / not-done(2) / in-progress(3)
```

### Update a task
```bash
python app.py update <id> "New description"
```

### Delete a task
```bash
python app.py delete <id>
```

### Change task status

**Mark as in progress**
```bash
python app.py mark-in-progress <id>
```

**Mark as done**
```bash
python app.py mark-done <id>
```

### List tasks

**List all**
```bash
python app.py list
```

**Filter**
```bash
python app.py list done
python app.py list todo
python app.py list in-progress
```

---

## Project Structure

```
.
├── task_cli.egg-info
├── .venv
├── setup.py
├── LICENSE
├── app.py
├── userdata.json
└── README.md
```

---

## Task Format

Example entry in `userdata.json`:

```json
{
  "id": 1,
  "description": "Example task",
  "status": "2",
  "createdAt": "...",
  "updatedAt": "..."
}
```

### Status values

```
1 → done
2 → todo
3 → in-progress
```
