#include "mainmenu.h"
#include "QtWidgets"
#include "cpage.h"
mainMenu::mainMenu()
{
    content = new QListWidget;
    stack = new QStackedWidget;
    content->setViewMode(QListView::IconMode);
    content->setIconSize(QSize(100,100));

    stack->addWidget(new Wallet);
    QGridLayout *glay = new QGridLayout;
    glay->addWidget(stack);
    this->setLayout(glay);
//    stack->addWidget();
//    stack->addWidget();
}
