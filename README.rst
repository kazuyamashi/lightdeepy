lightdeepy
==========

| Light Deep Learning on Python Git:
  https://github.com/kazuyamashi/lightdeepy.git
| Author: Kazushi Yamashina (Utsunomiya University)
| Contact: @KazushihuzaK (Twitter)

このリポジトリについて
======================

| このリポジトリは僕がDeep
  Learningの勉強用に作ったリポジトリです。公開しているソースコードは基本的に自由に使っていただいて構いません。使用した際はリファレンスとして紹介していただけると幸いです。
| なお、ここに公開している深層学習のプログラムは以下のURLに\ **安藤義裕**\ 様が公開していましたJavaScriptで実装されたコードをPythonで移植したものです。(素晴らしいコードの公開、大変感謝しております。)
| 今後、自分のオリジナリティを盛り込むべく開発していく予定です。
| `JavaScript で実装してみる Deep
  Learning <http://techblog.yahoo.co.jp/javascript/deep-learning-with-javascript/>`__

ディレクトリ構成
================

::

    dataset/
    lib/
    main/
    sublime/
    readme.md

-  dataset/

   -  Deep Learningに用いるデータセットの置き場所です。

-  lib/

   -  Deep
      Learningに用いるライブラリです。ライブラリについては順次コメント等追加したいと思います。

-  main/

   -  メインプログラムの置き場所です。

-  sublime/

   -  Sublime textのワークスペースの設定ファイルです。（自分用）

-  readme.md

**導入**

::

    git clone https://github.com/kazuyamashi/deep-learning.git
    cd deep-learning/

メインプログラム一覧
====================

learning\_fisher
~~~~~~~~~~~~~~~~

| 機械学習では有名（らしい）な\ `Fisher's Iris
  Data <http://www.math.uah.edu/stat/data/Fisher.html>`__\ のアヤメの計測データを用いた深層学習です。
| プログラムでは学習と判定をどちらも行っています。学習回数はcycle\_timeの引数として指定してください。
| **実行方法**　書式：``./learning_fisher.py input_file cycle_time``

::

    cd main/
    ./learning_fisher.py ../dataset/Fisher.txt 10000
