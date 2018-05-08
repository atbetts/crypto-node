#include <QApplication>

#include "mainmenu.h"

int main(int argc, char *argv[])
{


    QApplication app(argc, argv);
    app.setApplicationDisplayName("Cryptonode");
    mainMenu menu;
    return menu.exec();
}
