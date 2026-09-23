import streamlit as st


def main():
    st.title("注文入力チェック")
    st.write("すべての項目を入力し、「チェックする」を押してください。")
    st.caption("数量は1以上の整数で入力してください。例：1、10、100")

    # 項目名を順番に並べ、入力欄を作ります。
    names = ["会社名", "納品先", "受取人", "電話番号", "納期", "材料", "数量"]
    values = {}
    for name in names:
        values[name] = st.text_input(name).strip()

    if st.button("チェックする"):
        # 空白だけの入力も未入力として扱います。
        for name, value in values.items():
            if value == "":
                st.error(f"{name}が未入力です。入力してください。")
                return

        # 数量は数字だけで書かれた、1以上の整数を受け付けます。
        try:
            quantity = int(values["数量"])
        except ValueError:
            quantity = 0

        if not values["数量"].isdecimal() or quantity < 1:
            st.error("数量は1以上の整数で入力してください。0・負の数・小数・文字は使えません。")
            return

        st.success("入力内容に問題ありません。")
        st.subheader("入力内容一覧")
        for name, value in values.items():
            st.text(f"{name}：{value}")


if __name__ == "__main__":
    main()
