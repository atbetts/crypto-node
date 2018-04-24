#ifndef MAINMENU_H
#define MAINMENU_H

#include <QDialog>


QT_BEGIN_NAMESPACE
class QListWidget;
class QListWidgetItem;
class QStackedWidget;
QT_END_NAMESPACE


class mainMenu :
        public QDialog
{
    Q_OBJECT
    public : mainMenu();

    public slots:

    private:
        QStackedWidget *stack;
        QListWidget *content;
};






#endif // MAINMENU_H
