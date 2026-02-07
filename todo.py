#!/usr/bin/env python3
"""
Beautiful CLI To-Do List Manager
A feature-rich task management tool with priorities, categories, and progress tracking
"""

import os
import json
from datetime import datetime
from pathlib import Path


class Colors:
    """ANSI color codes for beautiful terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    DIM = '\033[2m'


class TodoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file, create if doesn't exist"""
        if not os.path.exists(self.filename):
            self.tasks = []
            self.save_tasks()
            print(f"{Colors.GREEN}✓ Created new tasks file: {self.filename}{Colors.END}\n")
        else:
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []
                print(f"{Colors.YELLOW}⚠ Warning: Invalid file format. Starting fresh.{Colors.END}\n")
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description, priority="medium", category="general"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority.lower(),
            "category": category.lower(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"{Colors.GREEN}✓ Task added successfully!{Colors.END}")
        self.display_task(task)
    
    def list_tasks(self, show_completed=False, category=None, priority=None):
        """Display all tasks with beautiful formatting"""
        filtered_tasks = self.tasks
        
        # Apply filters
        if not show_completed:
            filtered_tasks = [t for t in filtered_tasks if not t["completed"]]
        if category:
            filtered_tasks = [t for t in filtered_tasks if t["category"] == category.lower()]
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority.lower()]
        
        if not filtered_tasks:
            print(f"{Colors.DIM}No tasks found.{Colors.END}")
            return
        
        # Display header
        self.print_header()
        
        # Group by priority
        priorities = {"high": [], "medium": [], "low": []}
        for task in filtered_tasks:
            priorities.get(task["priority"], priorities["medium"]).append(task)
        
        # Display tasks by priority
        for priority_level, tasks_list in priorities.items():
            if tasks_list:
                priority_color = self.get_priority_color(priority_level)
                print(f"\n{priority_color}{Colors.BOLD}▶ {priority_level.upper()} PRIORITY{Colors.END}")
                for task in tasks_list:
                    self.display_task(task)
    
    def display_task(self, task):
        """Display a single task with beautiful formatting"""
        status_icon = "✓" if task["completed"] else "○"
        status_color = Colors.GREEN if task["completed"] else Colors.CYAN
        priority_color = self.get_priority_color(task["priority"])
        
        # Task line
        task_line = f"{status_color}{status_icon}{Colors.END} "
        task_line += f"{Colors.BOLD}[{task['id']}]{Colors.END} "
        
        if task["completed"]:
            task_line += f"{Colors.DIM}{task['description']}{Colors.END}"
        else:
            task_line += f"{task['description']}"
        
        print(f"  {task_line}")
        
        # Metadata line
        metadata = f"    {Colors.DIM}├─ Priority: {priority_color}{task['priority']}{Colors.END}{Colors.DIM}"
        metadata += f" │ Category: {Colors.CYAN}{task['category']}{Colors.END}{Colors.DIM}"
        metadata += f" │ Created: {task['created_at']}{Colors.END}"
        
        if task["completed"] and task["completed_at"]:
            metadata += f"{Colors.DIM} │ {Colors.GREEN}Completed: {task['completed_at']}{Colors.END}"
        
        print(metadata)
    
    def get_priority_color(self, priority):
        """Get color based on priority"""
        colors = {
            "high": Colors.RED,
            "medium": Colors.YELLOW,
            "low": Colors.BLUE
        }
        return colors.get(priority, Colors.YELLOW)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        task = self.find_task(task_id)
        if task:
            task["completed"] = True
            task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.save_tasks()
            print(f"{Colors.GREEN}✓ Task #{task_id} marked as complete!{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Task #{task_id} not found.{Colors.END}")
    
    def uncomplete_task(self, task_id):
        """Mark a task as incomplete"""
        task = self.find_task(task_id)
        if task:
            task["completed"] = False
            task["completed_at"] = None
            self.save_tasks()
            print(f"{Colors.CYAN}○ Task #{task_id} marked as incomplete.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Task #{task_id} not found.{Colors.END}")
    
    def update_task(self, task_id, description=None, priority=None, category=None):
        """Update task details"""
        task = self.find_task(task_id)
        if task:
            if description:
                task["description"] = description
            if priority:
                task["priority"] = priority.lower()
            if category:
                task["category"] = category.lower()
            self.save_tasks()
            print(f"{Colors.GREEN}✓ Task #{task_id} updated!{Colors.END}")
            self.display_task(task)
        else:
            print(f"{Colors.RED}✗ Task #{task_id} not found.{Colors.END}")
    
    def delete_task(self, task_id):
        """Delete a task"""
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            # Reindex tasks
            for idx, t in enumerate(self.tasks, 1):
                t["id"] = idx
            self.save_tasks()
            print(f"{Colors.RED}✗ Task #{task_id} deleted.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Task #{task_id} not found.{Colors.END}")
    
    def find_task(self, task_id):
        """Find a task by ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def search_tasks(self, keyword):
        """Search tasks by keyword"""
        results = [t for t in self.tasks if keyword.lower() in t["description"].lower()]
        
        if results:
            print(f"{Colors.CYAN}Found {len(results)} task(s) matching '{keyword}':{Colors.END}\n")
            for task in results:
                self.display_task(task)
        else:
            print(f"{Colors.DIM}No tasks found matching '{keyword}'.{Colors.END}")
    
    def get_stats(self):
        """Display statistics"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        pending = total - completed
        
        if total == 0:
            completion_rate = 0
        else:
            completion_rate = (completed / total) * 100
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}📊 STATISTICS{Colors.END}")
        print(f"{'─' * 50}")
        print(f"  Total Tasks:     {Colors.BOLD}{total}{Colors.END}")
        print(f"  {Colors.GREEN}✓{Colors.END} Completed:   {Colors.GREEN}{completed}{Colors.END}")
        print(f"  {Colors.CYAN}○{Colors.END} Pending:      {Colors.CYAN}{pending}{Colors.END}")
        print(f"  Completion Rate: {Colors.YELLOW}{completion_rate:.1f}%{Colors.END}")
        
        # Progress bar
        bar_length = 30
        filled = int(bar_length * completion_rate / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"  Progress: [{Colors.GREEN}{bar}{Colors.END}]")
        print(f"{'─' * 50}\n")
    
    def print_header(self):
        """Print beautiful header"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'═' * 60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}  📝 YOUR TASKS{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'═' * 60}{Colors.END}")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t["completed"]]
        # Reindex
        for idx, t in enumerate(self.tasks, 1):
            t["id"] = idx
        self.save_tasks()
        removed = before - len(self.tasks)
        print(f"{Colors.GREEN}✓ Cleared {removed} completed task(s).{Colors.END}")


def print_menu():
    """Display the main menu"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}║     CLI TO-DO LIST MANAGER v1.0        ║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}╚════════════════════════════════════════╝{Colors.END}\n")
    
    menu_items = [
        ("1", "Add Task", "➕"),
        ("2", "List Tasks", "📋"),
        ("3", "Complete Task", "✓"),
        ("4", "Update Task", "✏️"),
        ("5", "Delete Task", "🗑️"),
        ("6", "Search Tasks", "🔍"),
        ("7", "Show Statistics", "📊"),
        ("8", "Show All (including completed)", "📜"),
        ("9", "Clear Completed Tasks", "🧹"),
        ("0", "Exit", "👋")
    ]
    
    for num, desc, icon in menu_items:
        print(f"  {Colors.BOLD}{num}.{Colors.END} {icon}  {desc}")
    
    print(f"\n{Colors.DIM}{'─' * 42}{Colors.END}")


def main():
    """Main application loop"""
    todo = TodoList()
    
    while True:
        print_menu()
        choice = input(f"\n{Colors.BOLD}Choose an option: {Colors.END}").strip()
        
        print()  # Empty line for spacing
        
        if choice == "1":
            # Add task
            description = input(f"{Colors.CYAN}Task description: {Colors.END}").strip()
            if not description:
                print(f"{Colors.RED}✗ Description cannot be empty.{Colors.END}")
                continue
            
            priority = input(f"{Colors.CYAN}Priority (high/medium/low) [medium]: {Colors.END}").strip() or "medium"
            category = input(f"{Colors.CYAN}Category [general]: {Colors.END}").strip() or "general"
            
            todo.add_task(description, priority, category)
        
        elif choice == "2":
            # List tasks
            category = input(f"{Colors.CYAN}Filter by category (leave empty for all): {Colors.END}").strip() or None
            priority = input(f"{Colors.CYAN}Filter by priority (high/medium/low, leave empty for all): {Colors.END}").strip() or None
            todo.list_tasks(category=category, priority=priority)
        
        elif choice == "3":
            # Complete task
            try:
                task_id = int(input(f"{Colors.CYAN}Task ID to complete: {Colors.END}").strip())
                todo.complete_task(task_id)
            except ValueError:
                print(f"{Colors.RED}✗ Invalid task ID.{Colors.END}")
        
        elif choice == "4":
            # Update task
            try:
                task_id = int(input(f"{Colors.CYAN}Task ID to update: {Colors.END}").strip())
                description = input(f"{Colors.CYAN}New description (leave empty to keep current): {Colors.END}").strip() or None
                priority = input(f"{Colors.CYAN}New priority (leave empty to keep current): {Colors.END}").strip() or None
                category = input(f"{Colors.CYAN}New category (leave empty to keep current): {Colors.END}").strip() or None
                todo.update_task(task_id, description, priority, category)
            except ValueError:
                print(f"{Colors.RED}✗ Invalid task ID.{Colors.END}")
        
        elif choice == "5":
            # Delete task
            try:
                task_id = int(input(f"{Colors.CYAN}Task ID to delete: {Colors.END}").strip())
                confirm = input(f"{Colors.YELLOW}Are you sure? (y/n): {Colors.END}").strip().lower()
                if confirm == 'y':
                    todo.delete_task(task_id)
                else:
                    print(f"{Colors.DIM}Cancelled.{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}✗ Invalid task ID.{Colors.END}")
        
        elif choice == "6":
            # Search tasks
            keyword = input(f"{Colors.CYAN}Search keyword: {Colors.END}").strip()
            if keyword:
                todo.search_tasks(keyword)
            else:
                print(f"{Colors.RED}✗ Please enter a search term.{Colors.END}")
        
        elif choice == "7":
            # Show statistics
            todo.get_stats()
        
        elif choice == "8":
            # Show all tasks including completed
            todo.list_tasks(show_completed=True)
        
        elif choice == "9":
            # Clear completed tasks
            confirm = input(f"{Colors.YELLOW}Clear all completed tasks? (y/n): {Colors.END}").strip().lower()
            if confirm == 'y':
                todo.clear_completed()
            else:
                print(f"{Colors.DIM}Cancelled.{Colors.END}")
        
        elif choice == "0":
            # Exit
            print(f"{Colors.GREEN}Thanks for using CLI To-Do List Manager! 👋{Colors.END}\n")
            break
        
        else:
            print(f"{Colors.RED}✗ Invalid option. Please try again.{Colors.END}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}Thanks for using CLI To-Do List Manager! 👋{Colors.END}\n")
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {e}{Colors.END}\n")