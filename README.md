### Directory Description

    + Model: Optimizer, Logistic Regression, weight+
    
      Optimizer: SGD 기반의 방법론으로 파라미터를 업데이트 할 때, 사용되는 모듈입니다.
      Logistic Regression: 로지스틱 회귀분석을 구현한 클래스가 있습니다.
      weight: 모델의 coefficient를 (weight)를 저장한 pkl파일이 존재합니다.
      
    + Preprocessing: preprocessing+
      preprocessing: 분석에 사용될 columns을 선택한 뒤, Onehot encoding하여 array로 변환해주는 모듈입니다.
      
    + Result: Train_result, Test_result+
      train_result: 훈련데이터 전체 결과값 <Line Index> <Target Label> <Predict Probability> columns으로 구성되어 있습니다.
      Test_result: train_result 와 동일합니다.
    
    + templates: output, upload, Train_upload+
      output: Web Page에서 결과값을 화면에 출력하기 위해 필요한 html template입니다.
      upload: Web Page에서 로컬 환경에 있는 파일을 받기 위해 필요한 html template입니다.
    
    + Train_data: CriteoSearchDat+
      CriteoSearchData: 훈련용 데이터셋입니다.
    
    + app: webpage를 구현하기 위해 main함수의 역할을 하고 있습니다.
    
    + key, key_light: 데이터에 포함된 category 정보입니다.
    
### Prediction Model (Logistic Regression) Description (딥러닝 프레임워크 (tensorflow, pytorch), 머신러닝 프레임워크 sklearn, statsmodels 등 을 활용하지 X)

    + Model/Logistic_regression.py

*입력 받는 초기값 인자: Data(data), array상의 y 컬럼 인덱스(y_col_idx), 모델 저장 경로(save_dir)

==메서드 설명==
Logistic_MLE: 로지스틱 회귀의 최대 로그 우도 추정량 (Cost function)을 나타낸 것입니다. 원래 우도함수는 아래 그림과 같으나, 로그를 씌어 놓았기 때문에 메서드안의 return값에서 y값이 지수값에 포함된 것이 아니라 밑 값으로 계산 되는것을 확인 할 수 있습니다.

<img src="./Picture(MD 그림파일)/Likelihood.PNG">

Train: 로지스틱 회귀모형을 학습시키는 메서드입니다. Stochastic Gradient 기법을 통해 학습하였습니다.

predict_proba: 각 인스턴스의 CVR 확률값을 도출하기 위해 사용되는 메서드입니다.

predict: predict_proba의 확률값을 기준으로 0.5이상의 값을 1, 0.5이하의 값은 0으로 이진 분류하는 메서드입니다. return값으로 인스턴스의 예측 label을 반환합니다.

model_load: weight 폴더안에 있는 coefficient(weight) 정보를 가져오는 메서드입니다. (pkl 파일의 형태로 weight를 저장하고 내보냅니다.)

model_save: 학습된 모델의 coefficient(weight) 정보를 weight 폴더에 저장하는 메서드입니다. (pkl 파일)

result_saver: Result폴더로 Line number, Target label, Prediction probability가 명시된 txt 파일을 저장합니다. 
입력받는 인자는 현재 추론 상황이 Train인지 Test인지를 구별해주는 Learning_phase 가 있습니다. (아래 그림은 실제 출력 형태)

<img src="./Picture(MD 그림파일)/result캡처.PNG" height="50%" width="50%">

==실행 방법==

다음과 같은 방법으로 입력해주시면 로지스틱 회귀모형이 동작합니다.

<img src="./Picture(MD 그림파일)/Operating_method.PNG">

1) 로지스틱 회귀모형을 불러와 
2) weight의 경로에 있는 값을 load하고
3) 그 값을 Result폴더에 저장합니다. 

클래스를 생성할 때, data를 입력받기 때문에 예측값을 확인하고자 하는 경우에는 lr.predict()로 메서드를 호출하시면 예측값을 바로 출력하도록 구성하였습니다.

<img src="./Picture(MD 그림파일)/predict.PNG">

    + Model/Optimizer.py
    
*입력 받는 초기값 인자: 손실함수 값(Cost_func), weight parameter(coef), X값, y값, 학습률(learning_rate), epoch, batch_size, 학습할 때 데이터를 섞을지(shuffle), 학습이 중단되는 cost 수준(stop_cost_thres)

==메서드 설명==

minimize: 그래디언트를 계산하여 parameter를 업데이트 해주는 메서드입니다. Cost_func의 값을 미분하면 아래 그림과 같은 식으로 표현할 수 있습니다.

<img src="./Picture(MD 그림파일)/gradient.PNG">

이를 이용하여 Descent 방식으로 학습을 하는 코드 부분은 실제 코드상에서 노란색으로 표시된 부분과 같습니다.

<img src="./Picture(MD 그림파일)/training phase.PNG">

- Ascend방식으로 parameter를 업데이트하지 않은 이유는 MLE cost function에 (-)값을 붙여주어 목적 함수값을 최소화하면 실제 mle가 최대화 할 수 있게    Logistic_MLE의 return값을 설정해놓았기 때문입니다. (따라서 descent방식으로 학습 진행)


### Web Service
    
    + app.py
    
==함수 설명==

render_file: 입력 받은 line인자를 /get/cvr로 페이지로 넘겨주는 역할을 수행합니다. render_template을 이용해 upload.html을 가져와 웹 화면에 보여줍니다.
실제 웹 상에서의 동작 화면은 아래 그림과 같습니다.

1)

<img src="./Picture(MD 그림파일)/web1.PNG">

2)

<img src="./Picture(MD 그림파일)/web2.PNG" height="50%" width="50%">

3)

<img src="./Picture(MD 그림파일)/web3.PNG" height="50%" width="50%">


upload_file: /html/cvr.html 에서 request으로 upload 받은 인자를 이용하여 예측을 수행합니다. 수행된 결과는 Result값에 저장이 되고 웹 페이지상에 해당 결과값을 출력합니다.

<img src="./Picture(MD 그림파일)/web4.PNG" height="50%" width="50%">

upload: 입력 받은 line 인자를 /update/model 페이지로 넘겨주는 역할을 수행합니다. 이를 이용해 모형을 업데이트 합니다.

update: upload에서 받은 인자를 이용하여 실제 모형을 학습시키는 부분입니다. 학습이 정상적으로 종료되면 다음과 같이 화면에 출력됩니다.

<img src="./Picture(MD 그림파일)/web5.PNG">

== 실행 방법 ==

1)먼저 터미널환경에서 메인 함수 경로로 들어가 python app.py라고 실행

<img src="./Picture(MD 그림파일)/web_operating.PNG">

2)URL을 인터넷 창에 copy & paste (포트 번호 5000번 URL 주소)

<img src="./Picture(MD 그림파일)/web_operating2.PNG">


### 모형 성능 (데이터를 분할하여 추론)

==Train Data(백만건)==

<img src="./Picture(MD 그림파일)/train_metrics.PNG" height="30%" width="30%">

==Test Data(오십만건)==

<img src="./Picture(MD 그림파일)/test_metrics.PNG" height="30%" width="30%">

### 참고 사항

''' comment '''


데이터를 전부를 곧바로 집어넣고 바로 분석 결과를 도출하려 하였지만, 현재 로컬 환경 컴퓨터 리소스 자원이 충분하지 못한 관계(RAM:8GB)로 Chunknize하여 결과를 도출하였습니다. 위 결과는 result.ipynb파일에 남겨 놓았습니다.
