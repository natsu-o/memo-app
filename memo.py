def write_memo():
    memo = input("メモを入力してください: ")
    with open("memo.txt","a", encoding="utf-8") as f:
        f.write(memo + "\n")
    print("メモを保存しました。")

def read_memo():
    try:
        with open("memo.txt", "r", encoding="utf-8") as f:
            memos = f.readlines()
        print("\n★★ メモ一覧 ★★")
        for i, memo in enumerate(memos, 1):
            print(f"{i}. {memo.strip()}")
        print("----------------")
    except FileNotFoundError:
        print("まだメモがありません。")

def delete_memo():
    try:
        with open("memo.txt", "r", encoding="utf-8") as f:
            memos = f.readlines()

        if not memos:
            print("削除できるメモがありません。")
            return

        print("\n★★ メモ一覧 ★★")
        for i, memo in enumerate(memos, 1):
            print(f"{i}. {memo.strip()}")

        index = input("削除したいメモの番号を入力してください: ")

        if not index.isdigit() or int(index) < 1 or int(index) > len(memos):
            print("無効な番号です。")
            return

        deleted = memos.pop(int(index) - 1)

        with open("memo.txt", "w", encoding="utf-8") as f:
            f.writelines(memos)

        print(f"「{deleted.strip()}」を削除しました。")
    except FileNotFoundError:
        print("まだメモがありません。")


def main():
    while True:
        print("\n--- メモ帳メニュー ---")
        print("1. メモを書く")
        print("2. メモを見る")
        print("3. メモを削除する")
        print("4. 終了する")

        choice = input("番号を選んでください: ")

        if choice == "1":
            write_memo()
        elif choice == "2":
            read_memo()
        elif choice == "3":
            delete_memo()
        elif choice =="4":
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度入力してください。")

if __name__ == "__main__":
    main()
    
