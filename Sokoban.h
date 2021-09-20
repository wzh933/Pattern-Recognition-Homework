#ifndef BOXCIRNO_H
#define BOXCIRNO_H
#
#include <QPainter>
#include <QEvent>
#include <QKeyEvent>
#include <QString>
#include <QImage>
#include <QRect>
class Sokoban
{
private:
    int level=1;
    int step;
    int prestep;
public:
    Sokoban();
    void initMap();
    void initMap1();
    void initMap2();
    void initMap3();
    void initMap4();
    void initMap5();
    void initMap6();
    void initMap7();
    void initMap8();
    void initMap9();
    void initMap10();
    void initMap11();
//    void initMap();
//    void initMap();
//    void initMap();
//    void initMap();
    void drawMap(QPainter *pDraw);
    void keyDown(QKeyEvent *event);
    int getRow();
    int getCol();
    void setLevel(int l);
    void setStep(int s);
    bool gameOver();
    void remake();//重开
    void preStep();//上一步
    void preLev();//上一关
    void nextLev();//下一关

protected:
    int mp[8][8]=
    {
        {1, 1, 1, 1, 1, 1, 1, 1},
        {1, 3, 4, 0, 0, 0, 1, 1},
        {1, 0, 1, 1, 1, 0, 1, 1},
        {1, 0, 0, 5, 0, 0, 1, 1},
        {1, 0, 1, 4, 1, 0, 1, 1},
        {1, 0, 1, 3, 1, 0, 1, 1},
        {1, 0, 0, 0, 4, 3, 1, 1},
        {1, 1, 1, 1, 1, 1, 1, 1}
    };
};


#endif // BOXCIRNO_H
