
# Learning Journal Unit 4 CS 1101

## Part 1

Section 6.2 of your textbook describes incremental development. Do the exercise at the end of that section:
As an exercise, use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments. Record each stage of the development process as you go. (Downey, 2015)
After the final stage of development, print the output of hypotenuse(3, 4) and two other calls to hypotenuse with different arguments.

#### Include all of the following in your Learning Journal:
An explanation of each stage of development, including code and any test input and output.
The output of hypotenuse(3, 4).
The output of two additional calls to hypotenuse with different arguments.

### Hypotenuse function
With this exercise I looked up the equation for finding a hypotenuse, then I translated it into code. For parameters I declared a and b as two sides of a triangle being used to calculate the third. The function returns a and b, each squared before being added, and then the sum of the two being returned. I then tested it out in a cloud Python notebook service with the inputs three and four.
```python
def find_hypotenuse(a, b):
    return a**2 + b**2

find_hypotenuse(3, 4)
find_hypotenuse(4, 3)
find_hypotenuse(12, 14)
find_hypotenuse(22.2, 45.2)
```
#### Output
```sh
25

25

340

2535.88
```

## Part 2

Invent your own function that does some useful computation of your choosing. Do not copy the function from somewhere else. Use incremental development, and record each stage of the development process as you go. Finally, print output that demonstrates that the function works as you intended.

Include all of the following in your Learning Journal:

An explanation of each stage of development, including code and any test input and output.
The output of three calls to your function with different arguments.

Function calls are at the bottom of included .py file, the output for those function calls are immediately below.

Output:
{
    'mean': 24.628837421891273,
    'std_dev': 21.375217340181205,
    'variance': 456.89991633998324,
    'skewness': 987.4802639265737,
    'kurtosis': 35240.99893472802,
    'z_scores': [-1.1522145964613844, -1.1389558520736804, -1.0650898853897168, -1.1312707856649913, -1.0738987901010928, -1.100369340722268, -1.0737456648223274, -0.9940642193645367, -1.1283317428684092, -0.8026336690725603, -0.7762508612948024, -0.9649631583557752, -0.8357805501299314, -0.5543486497621978, -0.9345045137636518, -0.9828738575417778, -0.586603951838792, -1.1104129818667745, -0.3986248380127786, -0.4085653192187202, -0.27144412775028554, -0.7162175294653834, -0.9942255994349224, -0.9391768523523154, -0.729965177135756, -1.1213052247487156, -0.01092807197458514, -0.9347475533009685, 0.1360707617107793, -0.07276820503599218, -0.038597117321451796, 0.24864149770133667, -0.507501022969949, -0.12523822673635748, -1.0636614742074393, -0.7305771557963724, 0.15063600506595093, -0.1419033011578617, 0.28582406672341404, -0.7635772109822305, 0.6743140125437336, 0.7059065064618609, 0.6739159192404218, -0.801782925726248, -0.9423869151193005, -0.1526284993975789, 0.9490385476085909, -0.9154153035481263, 0.7688668723332008, 1.045410311715356, -0.6505822803427047, -0.3150721522786878, 0.15604323303534426, -0.969042388657319, 1.0142094599455607, -0.47750093527030174, 0.7174653803679557, 1.4001050904459194, 0.5175556800674477, -0.8082510402401142, 0.9716223372497934, -0.28007127902131357, 1.1206834360511186, -0.9630202902384754, -0.09483228072350937, 0.5924064812115681, 0.586488876111659, 0.622640139126642, 0.5642458741584655, 1.0597125464945227, -0.3504889324234233, -0.5208164167264563,
        1.440306088615805, 0.8560268765322616, -0.7797644506759381, 0.0714783983020578, 1.4330544545670776, 0.620263469435508, -0.7168701587857501, -0.40444173493495156, 1.9154779365622239, 0.30953850827063245, 0.039020037411245344, 2.170878044975555, 1.3132618358226833, -0.32692726655021054, 0.24843923180704047, 1.279154697907068, 0.3480714427907274, 1.8449293229555135, 1.39367408546622, 3.0926542009943554, -0.48976857661901824, 3.122762918312471, 0.2766106453702638, -0.6994174996057407, -0.909950312724008, 2.6185493473895263, -1.0759885720174784, 1.664402711464517
    ],
    'std_err': 2.1375217340181205
} {
    'mean': 13.795059631029126,
    'std_dev': 12.997247211007856,
    'variance': 168.9284350640515,
    'skewness': 315.0622205504705,
    'kurtosis': 7003.320754078291,
    'z_scores': [-1.0613831842288552, -1.0355271558622186, -0.9178200287864419, -1.0160928893062349, -0.8683827613112998, -1.035278549290518, -0.8538179461794301, -0.6786793954983177, -0.9617705524562528, -1.0570006173750484, -1.057150068831657, -0.7732951969548385, -0.6918112315309195, -0.7468163073289849, -0.13845695381376966, -0.7407928848958584, -0.6785318391844658, 0.0236707926075747, -0.6843067320465082, -0.5134330465629415, -0.3661939708476313, -0.20346039019951023, -0.14760935969013883, 0.6109540884873796, 0.45274003125877293, 0.42924546507978945, 0.9325959939129219, -0.11882051959307749, 0.6458308390214208, 1.147489854918391, 0.9992297659219699, -0.8275261841297145, -0.8781256299037189, 0.239832024163706, -0.8874854230506808, 0.04654441276779808, -0.30909239660548365, -0.4624756894662918, 1.1376391405357784, 1.003372882468148, 0.6048671230468604, 1.7203432157934395, -0.70776532511575, -0.4302982919441032, 1.532044533653679, 0.9519693210717947, 1.3777820249694686, 2.510504873334409, 1.82063517048128, 2.661908968496076],
    'std_err': 1.8380883279323195
} {
    'mean': 9.5,
    'std_dev': 5.916079783099616,
    'variance': 35.0,
    'skewness': 0.0,
    'kurtosis': 647.6285714285714,
    'z_scores': [-1.6057930839841814, -1.4367622330384782, -1.267731382092775, -1.0987005311470714, -0.9296696802013682, -0.760638829255665, -0.5916079783099616, -0.4225771273642583, -0.253546276418555, -0.08451542547285165, 0.08451542547285165, 0.253546276418555, 0.4225771273642583, 0.5916079783099616, 0.760638829255665, 0.9296696802013682, 1.0987005311470714, 1.267731382092775, 1.4367622330384782, 1.6057930839841814],
    'std_err': 1.3228756555322954
}

## Part 3

Describe your experience so far with peer assessment of Discussion Assignments.

How do you feel about the feedback and ratings you have received from your peers?
How do you think your peers feel about the feedback you provided them? And the ratings you gave them?
Reference:  

Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.

Everything having to do with the peer review system and discussion assignments work well and I haven't had any issues with but one. However what I do have an issue with is Moodle. Moodle isn't very user friendly when it comes to the discussion forums, it should be much easier and faster to use. Giving feedback and responding to it should be fast and efficient, like a social media service such as Twitter. Otherwise it creates a lag in the forum and puts a stopper into any real discussion. The notification system with subscription sometimes doesn't really seem to work, it would be better if every time there was a new post created you received a notification on your phone for example. Another issue with that is every time you do go to check Moodle's class forums, is having to scroll through every single post. Having to search through everything just to find a response to your post isn't a very good way to work, especially for people like me who always has something to do and doesn't have time to check Moodle every hour. I really wish I could have conversations on the discussion forums as easy and fast as text messages, students will miss out because of it. This affects every aspect of peer assessment, it isn't terrible but it should be better.