import PySimpleGUI as sg
import os

# 1. 登録が必要なバージョン5系の場合、ここでライセンス入力を求められます
# 2. フラッシュ対策：ダブルバッファリング的な挙動を期待してテーマを固定
sg.theme('SystemDefault') 

def create_tab(title="無題", content="", path=None):
    uid = os.urandom(4).hex()
    # キーを単純な文字列にして認識率を上げる
    return sg.Tab(title, [
        [sg.Multiline(content, font=('Consolas', 11), key=f'BODY_{uid}', 
                     expand_x=True, expand_y=True)]
    ], key=f'TAB_{uid}', metadata={'path': path, 'body': f'BODY_{uid}'})

# 初期のタブを用意
initial_tab = create_tab()
layout = [
    [sg.Menu([['&File', ['&New Tab', '&Open', '&Save', 'E&xit']]])],
    [sg.TabGroup([[initial_tab]], key='-TG-', expand_x=True, expand_y=True)],
    [sg.Button('＋ 新規', key='-ADD-'), sg.Button('閉じる', key='-CLOSE-')]
]

# finalize=True に加え、keep_on_topで描画を安定させる（任意）
window = sg.Window("Memo Pro", layout, resizable=True, size=(700, 450), finalize=True)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    # 現在のタブを特定
    curr_tab_key = values.get('-TG-')
    
    # --- 新規タブ ---
    if event in ('-ADD-', 'New Tab'):
        new_tab = create_tab()
        window['-TG-'].add_tab(new_tab)
        new_tab.select()
        window.refresh() # 追加後に強制描画

    # --- ファイルを開く ---
    if event == 'Open':
        path = sg.popup_get_file('ファイルを開く', no_window=True)
        if path:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            new_tab = create_tab(os.path.basename(path), content, path)
            window['-TG-'].add_tab(new_tab)
            new_tab.select()
            window.refresh()

    # --- 保存 ---
    if event == 'Save':
        if curr_tab_key:
            curr_tab_obj = window[curr_tab_key]
            path = curr_tab_obj.metadata['path']
            if not path:
                path = sg.popup_get_file('保存', save_as=True, no_window=True, default_extension=".txt")
            
            if path:
                body_key = curr_tab_obj.metadata['body']
                # values[body_key] が取れない場合への対策
                content = window[body_key].get() 
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                curr_tab_obj.update(title=os.path.basename(path))
                curr_tab_obj.metadata['path'] = path
                sg.popup_quick_message('保存完了')

    # --- タブを閉じる ---
    if event == '-CLOSE-':
        if len(window['-TG-'].get_list()) > 1:
            window[curr_tab_key].close()

window.close()
