# 📝 Beautiful CLI To-Do List Manager

A feature-rich, visually stunning command-line task management application built with Python. Track your tasks with style using colors, priorities, categories, and more!

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)

## ✨ Features

- 🎨 **Beautiful Interface** - Color-coded priorities and elegant formatting
- 📊 **Task Priorities** - Organize tasks as high, medium, or low priority
- 🏷️ **Categories** - Group tasks by custom categories
- 🔍 **Smart Search** - Quickly find tasks by keyword
- 📈 **Statistics Dashboard** - Track your productivity with completion rates
- ⚡ **Quick Actions** - Add, update, complete, and delete tasks easily
- 💾 **Auto-Save** - All changes saved automatically to a JSON file
- 🎯 **Filtering** - View tasks by category or priority
- 📅 **Timestamps** - Track when tasks were created and completed

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/cli-todo-list.git
cd cli-todo-list
```

2. Run the application:
```bash
python todo.py
```

That's it! No dependencies required - uses only Python standard library.

## 📖 Usage

### Main Menu

When you run the application, you'll see an interactive menu:

```
╔════════════════════════════════════════╗
║     CLI TO-DO LIST MANAGER v1.0        ║
╚════════════════════════════════════════╝

  1. ➕  Add Task
  2. 📋  List Tasks
  3. ✓   Complete Task
  4. ✏️   Update Task
  5. 🗑️   Delete Task
  6. 🔍  Search Tasks
  7. 📊  Show Statistics
  8. 📜  Show All (including completed)
  9. 🧹  Clear Completed Tasks
  0. 👋  Exit
```

### Adding a Task

```bash
Choose option: 1
Task description: Complete project documentation
Priority (high/medium/low) [medium]: high
Category [general]: work
```

### Viewing Tasks

Tasks are automatically organized by priority with beautiful color coding:

```
▶ HIGH PRIORITY
  ○ [1] Complete project documentation
    ├─ Priority: high │ Category: work │ Created: 2025-02-07 14:30

▶ MEDIUM PRIORITY
  ✓ [2] Buy groceries
    ├─ Priority: medium │ Category: personal │ Created: 2025-02-07 10:15
    │ Completed: 2025-02-07 15:20
```

### Completing Tasks

```bash
Choose option: 3
Task ID to complete: 1
✓ Task #1 marked as complete!
```

### Updating Tasks

```bash
Choose option: 4
Task ID to update: 1
New description (leave empty to keep current): Finish documentation
New priority (leave empty to keep current): medium
New category (leave empty to keep current): 
✓ Task #1 updated!
```

### Searching Tasks

```bash
Choose option: 6
Search keyword: project
Found 2 task(s) matching 'project':
  ○ [1] Complete project documentation
  ○ [3] Start new project
```

### Statistics

View your productivity metrics:

```
📊 STATISTICS
──────────────────────────────────────────────────
  Total Tasks:     10
  ✓ Completed:     6
  ○ Pending:       4
  Completion Rate: 60.0%
  Progress: [████████████████████░░░░░░░░░░]
──────────────────────────────────────────────────
```

## 🎨 Color Scheme

- 🔴 **Red** - High priority tasks
- 🟡 **Yellow** - Medium priority tasks
- 🔵 **Blue** - Low priority tasks
- 🟢 **Green** - Completed tasks and success messages
- 🔵 **Cyan** - Active/pending tasks and prompts

## 📁 Data Storage

Tasks are stored in `tasks.txt` in JSON format. The file is automatically created on first run and updated whenever you make changes.

Example `tasks.txt` structure:
```json
[
  {
    "id": 1,
    "description": "Complete project documentation",
    "priority": "high",
    "category": "work",
    "completed": false,
    "created_at": "2025-02-07 14:30",
    "completed_at": null
  }
]
```

## 🛠️ Advanced Usage

### Filtering Tasks

When listing tasks, you can filter by:
- **Category**: Show only tasks from a specific category
- **Priority**: Show only high, medium, or low priority tasks

### Batch Operations

- **Clear Completed**: Remove all completed tasks at once
- **Show All**: View both pending and completed tasks

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -am 'Add feature'`
6. Push: `git push origin feature-name`
7. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Inspired by the need for beautiful, functional CLI tools
- Thanks to the open-source community

## 📮 Contact

Have questions or suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Star ⭐ this repository if you find it useful!

---

**Happy Task Managing! 🎉**
