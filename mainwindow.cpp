#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setFixedSize(8*64,8*64);
    pBox=new Sokoban;
    pMap=new QPainter(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::keyPressEvent(QKeyEvent *event)
{
    pBox->keyDown(event);
//    if(pBox->gameOver())
//    {
//        this->close();
//    }
}

void MainWindow::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event);
    pMap->begin(this);
    pBox->drawMap(pMap);
    pMap->end();
    update();
}
void MainWindow::mousePressEvent(QMouseEvent *event)
{}
