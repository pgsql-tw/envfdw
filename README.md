# envfdw
- envFDW 是一個 forign data wrapper，用於處理環境變數。
- 這些操作都只有在目前連線中有效，重新連線就會還原。
- 作為 FDW 開發者的入門範例。

## Installation
### Platform (Tested)
- Ubutnu Server 18.04 LTS
- PostgreSQL 11
   - Add PostgreSQL repository: https://www.postgresql.org/download/linux/ubuntu/
- Multicorn 1.3.4
   - https://multicorn.org/
- Python 3.6

### Install PostgreSQL and Multicorn
```
# apt-get install postgresql-11 postgresql-11-python3-multicorn
```

### Install envFDW
- 找到你環境中的 multicorn 路徑，本例為： /usr/lib/python3/dist-packages/multicorn
- 複製檔案 "envfdw.py" 到該路徑下。
- 用 symbolic link 也是可以的唷。

## Usages
- 連線進入你的 PostgreSQL 資料庫。
- 第一次使用要設定 FDW。
```
CREATE EXTENSION multicorn;
CREATE SERVER envfdw_srv FOREIGN DATA WRAPPER multicorn OPTIONS ( wrapper 'multicorn.envFDW.FDW' );
CREATE FOREIGN TABLE envfdw ( var text, val text ) SERVER envfdw_srv;
```
- 之後可以當作一般 Table 進行查詢。
```
SELECT * FROM envfdw; -- List all environment variables
INSERT INTO envfdw (var, val) VALUES ('abc', '1'), ('def', '2'); -- Add two new environment variables
UPDATE envfdw SET val='3' WHERE var='abc'; -- Set a new value to specified environment variables
DELETE FROM envfdw WHERE var='def'; -- Unset environment variables
```


