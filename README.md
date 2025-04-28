# 書法字庫

![莒光書法字庫 Demo](/assets//demo.gif)

這是一個書法字庫的開源空間，未來期望透過不同方法讓各界能共同編輯、維護這個字庫，並且補充字庫的內容。詳細的維護方式仍待討論，歡迎有興趣或想法的朋友們，加入我們的討論，亦可傳送電子郵件至 [hi@neillu.com](mailto:hi@neillu.com)。

> [!Tip]
> 若要試用此字庫，可以至[莒光書法字庫](https://jgwords.neillu.com)網站進行試用。

> [!Warning]
> - 本字庫的內容，依然有許多缺字的情形發生，使用時請注意。
> - 由於原字庫是 @zhuojg 以簡體中文作為資料夾索引，因此本專案中，仍然保留簡體中文的資料夾名稱，未來會考慮將其轉為繁體中文的資料夾名稱，或是提供簡繁轉換的功能。
> - 由於部分簡體字將不同反體字合併為同一字，在使用時，可能會有「不同繁體字被分配到同一資料夾」的情形發生，另請注意。
> - 若在使用時需要繁體與簡體文字間的轉換，請參考 [OpenCC](https://github.com/BYVoid/OpenCC) 專案。

## 資料來源與授權

### 最初來源

本網站所提供的字體與字庫合輯，來自 @zhuojg 所整理的字庫。其整理的過程中，或許對影像進行處理，並統整成字庫合輯。@zhuojg 將其字庫以 Apache License 2.0 授權，並且在 GitHub 發佈於 [Chinese Calligraphy Dataset](https://github.com/zhuojg/chinese-calligraphy-dataset) 專案中。

### 授權條款

請使用者在本網站使用字庫合輯時，遵守 Apache License 2.0 的條款。

## 貢獻字庫

歡迎直接在本專案中進行貢獻，或是聯絡 [hi@neillu.com](mailto:hi@neillu.com)。

## 附加軟體

### 軟體使用

這個專案中提供了一個 Python 檔案（`indexing.py`），可以將字庫中的資料夾結構與檔案名稱轉為一 JSON 格式的索引檔案。在確認 Python 環境後，直接執行該檔案即可。另外，也提供現成的索引檔案（`index.json`），可以直接使用。

```bash
python indexing.py
# or
python3 indexing.py
```

### 軟體授權

開發者並不保留對該 Python 檔案的著作權，使用者可以自由使用。唯 `index.json` 檔案的內容，仍然受到 Apache License 2.0 的授權條款約束。使用者在使用該檔案時，請遵守 Apache License 2.0 的條款。