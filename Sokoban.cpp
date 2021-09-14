#include "Sokoban.h"
#include "memory.h"

Sokoban::Sokoban()
{
    initMap();
}

void Sokoban::initMap()
{
    int g[8][8] ={
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 3, 4, 0, 0, 0, 1, 1},
    {1, 0, 1, 1, 1, 0, 1, 1},
    {1, 0, 0, 5, 0, 0, 1, 1},
    {1, 0, 1, 4, 1, 0, 1, 1},
    {1, 0, 1, 3, 1, 0, 1, 1},
    {1, 0, 0, 0, 4, 3, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1}
}; //地图
    memcpy(&mp[0][0],&g[0][0],sizeof (int)*64);
}

void Sokoban::drawMap(QPainter *pDraw)
{

    for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                QString imgURL;
                switch (mp[i][j])
                {
                case 0://空格
                    imgURL="://Qt_Images/white.png";
                    break;
                case 1://墙
                    imgURL="://Qt_Images/wall.jpg";
                    break;
                case 3://目的地
                    imgURL="://Qt_Images/moon.jpg";
                    break;
                case 4://箱子
                    imgURL="://Qt_Images/c++.png";
                    break;
                case 5://人
                case 8:
                    if (gameOver())
                        imgURL="://Qt_Images/p2.png";
                    else
                        imgURL="://Qt_Images/xiaoren.png";
                    break;
                case 7://箱子进去了
                    imgURL="://Qt_Images/luck.jpg";
                    break;

                default:
                    break;
                }
                //贴图
                QImage img(imgURL);
                pDraw->drawImage(QRect(j*img.width(),i*img.height(),img.width(),img.height()),img);
            }

        }

}

void Sokoban::keyDown(QKeyEvent *event)
{

        int i = getRow();
        int j = getCol();
        switch (event->key())
        {
        case Qt::Key_W:
        case Qt::Key_Up:
            if (mp[i - 1][j] == 0 || mp[i - 1][j] == 3)
            {
                mp[i][j] -= 5;     //人走了
                mp[i - 1][j] += 5; //人来了
            }
            if (mp[i - 1][j] == 4 || mp[i - 1][j] == 7) //人上是个箱子
            {
                if (mp[i - 2][j] == 0 || mp[i - 2][j] == 3) //箱子上是空的或目的地
                {
                    mp[i][j] -= 5;     //人走了
                    mp[i - 1][j] += 1; //人来了，下个地方综合起来加1
                    mp[i - 2][j] += 4;
                }
            }
            break;
        case Qt::Key_S:
        case Qt::Key_Down:
            if (mp[i + 1][j] == 0 || mp[i + 1][j] == 3)
            {
                mp[i][j] -= 5;
                mp[i + 1][j] += 5;
            }
            if (mp[i + 1][j] == 4 || mp[i + 1][j] == 7)
            {
                if (mp[i + 2][j] == 0 || mp[i + 2][j] == 3)
                {
                    mp[i][j] -= 5;
                    mp[i + 1][j] += 1; //人来了，下个地方综合起来加1
                    mp[i + 2][j] += 4;
                }
            }
            break;
        case Qt::Key_A:
        case Qt::Key_Left:
            if (mp[i][j - 1] == 0 || mp[i][j - 1] == 3)
            {
                mp[i][j] -= 5;
                mp[i][j - 1] += 5;
            }
            if (mp[i][j - 1] == 4 || mp[i][j - 1] == 7)
            {
                if (mp[i][j - 2] == 0 || mp[i][j - 2] == 3)
                {
                    mp[i][j] -= 5;
                    mp[i][j - 1] += 1; //人来了，下个地方综合起来加1
                    mp[i][j - 2] += 4;
                }
            }
            break;
        case Qt::Key_D:
        case Qt::Key_Right:
            if (mp[i][j + 1] == 0 || mp[i][j + 1] == 3)
            {
                mp[i][j] -= 5;
                mp[i][j + 1] += 5;
            }
            if (mp[i][j + 1] == 4 || mp[i][j + 1] == 7)
            {
                if (mp[i][j + 2] == 0 || mp[i][j + 2] == 3)
                {
                    mp[i][j] -= 5;
                    mp[i][j + 1] += 1; //人来了，下个地方综合起来加1
                    mp[i][j + 2] += 4;
                }
            }
            break;

        default:
            break;
        }
}

int Sokoban::getRow()
{
    for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                if (mp[i][j] == 5 || mp[i][j] == 8)
                    return i;
            }
        }
        return -1;
}

int Sokoban::getCol()
{
    for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                if (mp[i][j] == 5 || mp[i][j] == 8)
                    return j;
            }
        }
        return -1;
}

bool Sokoban::gameOver()
{
    for (int i = 0; i < 8; i++)
            for (int j = 0; j < 8; j++)
            {
                if (mp[i][j] == 3 || mp[i][j] == 4)
                    return false;
            }
    return true;
}








