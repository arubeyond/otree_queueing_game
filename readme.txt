設定：
　　T：時間
　　R, num_rounds：ラウンド数
　　N, players_per_group, num_demo_participants：被験者の総数
　　G：各ラウンドのグループの人数
	ポアソン到着は下4行
　　幾何サービスはclass Group: calc_waitingtime内の2行

〇models.py
make_matching：
　　全ラウンドのマッチング行列を作成
　　休みの回数の差は最大で１
　　Group１（0番目）は休みになる

Group：
　　social_payoff : 待ち時間の合計
　　overwork：時刻Tでのworkload
　　calc_waitingtime：
	ResultWaitPageで各グループにおいて実行

	それぞれの時刻ｔで
	　　workloadの消化
	　　arrival_players：時刻ｔに到着したプレイヤー集合
	　　シャッフル
	　　waiting_time, workloadの更新

Player：
　　arrival_time：到着時刻（０～Tで入力）
　　service_time：サービス時間（デフォルト４）
　　waiting_time：待ち時間

〇pages.py
Introduction：イントロダクション（ラウンド1のみ）
↓
StartWait：開始待ち（全員）
↓
DecideArrivalTime：到着時刻の入力（Group1以外）
↓
DecideWaitPage：入力待ち（全員）
↓
ResultsWaitPage：待ち時間の計算（Group1以外）
↓
Results：結果の表示（Group1以外）

〇これからの実装方針
HTMLをきれいにする
前後半の実験に対応可能にする
　　half_round=15
　　half_round以下ならサービス時間の変化なし
　　half_roundちょうどなら後半用のイントロダクションを表示
　　half_round以上ならサービス時間の変化あり
デモプレイ導入する
　　１～３、half_round～half_round＋２はデモプレイにしてみるとか？
