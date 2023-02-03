# Image Quality Assessment

LAST MODIFIED: 2023.02.03

Intro
---
IQA는 제가 학부생을 졸업하는 시점에 드디어 한 번도 써보지 못했던 논문을 써보면서 연구했던 영역입니다.  
저에게는 남다른 의미이자 뿌듯하고.. 짜증났고.. 아직까지 많은 부분들이 아쉬움이 남는 애증의 첫 논문인데요.  
비록 완성도가 높은 논문은 아닐지라도 연구하면서 배웠던 것들을 기록하는 의미에서 정리해보도록 하겠습니다.

WHAT IS IQA?
---
이미지의 품질을 정량화하려는 영역입니다. 이미지들이 뿌옇거나 살짝 회전이 되있다던지 그러한 이미지들을
인간의 시각 시스템(Human Visual System, 이하 HVS)에 의한 평가에서 벗어나 알고리즘, ML, DL에 의해 점수를 산정하려는 노력입니다.
대표적으로 PSNR, SSIM, BRISQUE가 존재하는데 최근엔 CNN이나 딥러닝 모델을 활용한 IQA 모델들이 많이 등장하고 있습니다.

BREFOLA
---
BREFOLA는 Blind/Referenceless via Fourier transform and Laplacian filter의 약자로.. 예.. 제가 논문에서 제안한 IQA 모델입니다.
이미지 픽셀 밝기값의 변화를 파형으로 보는 즉, 주파수 영역대로 변환하여 
