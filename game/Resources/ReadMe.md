eng:

#Made to be copypaste-imported into Renpy with  **CubismSdkForNative > 3.3** 
All and every animation made in three versions:
	fast
	med
	slo
All corresponding animation files are named respectfully
	<animname> fast/med/slo.motion3.json


#Usage in script:
script.rpy(defining):	image <animname> = Live2D('Resources/<animname>',base=<zoom lvl 0-1>,loop=True<all logically looping anims requre that>,seamless=True) //the "Resources" is a Native's musthave better follow that this..
options.rpy:	define config.gl2 = True
script.rpy(displaying):	 show <animname> <variant>



rus:
#Сделано для быстрого импорта в Renpy с **CubismSdkForNative > 4** 
Все и каждая анимации сделаны в трех версиях:
	fast
	med
	slo
Соответсвтующие каждому варианту файлы анимаций названны соответственно:
	<animname> fast/med/slow.motion.json


#Использование в коде:
script.rpy(определение переменных):	image <animname> = Live2D('Resources/<animname>',base=<zoom lvl 0-1>,loop=True<all logically looping anims requre that>,seamless=True) //the "Resources" is a Native's musthave better follow that this..
options.rpy:	define config.gl2 = True
script.rpy(отображение):	 show <animname> <variant>