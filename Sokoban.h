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
    int level;
    int step;
    int prestep;
public:
    Sokoban();
    void initMap();
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
