import json
import os
import sys

class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "完了" if self.completed else "未完了"
        return f"タスク: {self.name}\n説明: {self.description}\n状態: {status}"

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f"タスク '{name}' を追加しました。")

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"タスク '{name}' を削除しました。")
                return
        print(f"タスク '{name}' が見つかりません。")

    def list_tasks(self):
        if not self.tasks:
            print("タスクがありません。")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_task_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_completed()
                print(f"タスク '{name}' を完了にしました。")
                return
        print(f"タスク '{name}' が見つかりません。")

    def save_tasks(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([{
                    'name': task.name,
                    'description': task.description,
                    'completed': task.completed
                } for task in self.tasks], f, ensure_ascii=False, indent=4)
            print("タスクを保存しました。")
        except Exception as e:
            print(f"保存中にエラーが発生しました: {e}")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task(item['name'], item['description'], item['completed']) for item in data]
                print("タスクを読み込みました。")
            except Exception as e:
                print(f"読み込み中にエラーが発生しました: {e}")

def main():
    manager = TaskManager()

    while True:
        print("\n=== タスクマネージャー ===")
        print("1. タスクを追加")
        print("2. タスクを削除")
        print("3. タスク一覧を表示")
        print("4. タスクを完了にする")
        print("5. 終了")

        choice = input("選択してください (1-5): ").strip()

        if choice == '1':
            name = input("タスク名: ").strip()
            description = input("説明: ").strip()
            manager.add_task(name, description)
        elif choice == '2':
            name = input("削除するタスク名: ").strip()
            manager.remove_task(name)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            name = input("完了にするタスク名: ").strip()
            manager.mark_task_completed(name)
        elif choice == '5':
            manager.save_tasks()
            print("終了します。")
            break
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()