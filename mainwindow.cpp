#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setFixedSize(8*128,8*128);
    pBox=new Sokoban;
    pMap=new QPainter(this);
//    nextLevel=new QPushButton(QString("下一关"),this);
//    restart=new QPushButton(QString("重新开始"),this);
//    preLevel=new QPushButton(QString("上一关"),this);
//    goBackStep=new QPushButton(QString("回退"),this);

    menu=menuBar()->addMenu(tr("选项"));
    QAction *action=menu->addAction(tr("读取外部关卡"));
    menu->addSeparator();
    QAction *action4=menu->addAction(tr("上一步"));
    connect(action4,SIGNAL(triggered()),this,SLOT(onGoBackBtnClicked()));
    menu->addSeparator();

    QAction *action2=menu->addAction(tr("重新开始"));
    connect(action2,SIGNAL(triggered()),this,SLOT(onRestartBtnClicked()));
    menu->addSeparator();
    QAction *action3=menu->addAction(tr("上一关"));
    connect(action3,SIGNAL(triggered()),this,SLOT(onPreBtnClicked()));
    QAction *action1=menu->addAction(tr("下一关"));
    connect(action1,SIGNAL(triggered()),this,SLOT(onNextBtnClicked()));
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

void MainWindow::onGoBackBtnClicked()
{
    pBox->preStep();
}
void MainWindow::onRestartBtnClicked()
{
    pBox->remake();
}
