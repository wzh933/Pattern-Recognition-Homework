#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <Sokoban.h>

#include <QLabel>
#include <QTextEdit>
#include <QPushButton>
#include <QWidget>
#include <iostream>
#include <QTime>
#include <QLineEdit>
#include <QPushButton>
#include <QPainter>
#include <QMessageBox>
#include <QDebug>
#include <QKeyEvent>
#include <QPixmap>
#include <QMenuBar>
#include"Sokoban.h"
#include <QMenu>
#include <QThread>
#include <QMutex>
#include <QMutexLocker>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void keyPressEvent(QKeyEvent *event);
    void paintEvent(QPaintEvent *event);
    void mousePressEvent(QMouseEvent *event);



private:
    Ui::MainWindow *ui;
    QPainter *pMap;//地图
    Sokoban *pBox;//箱子

    QLabel *roundLabel;
    QLabel *stepLabel;
    QPushButton *preLevel;
    QPushButton *nextLevel;
    QPushButton *restart;
    QPushButton *goBackStep;

    QMenu *menu;
    QMutex mutex;

private slots:
//    void onNextBtnClicked();//下一关
    void onRestartBtnClicked();//重新开始
//    void onPreBtnClicked();//前一关
    void onGoBackBtnClicked();//回退
//    void onActionClicked();
//    void showHelpInformation();
//    void showAboutInformation();


};
#endif // MAINWINDOW_H
