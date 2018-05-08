#include <QHBoxLayout>
#include <QLabel>
#include <QString>

#include "cpage.h"

Wallet::Wallet(QWidget *parent): QWidget(parent){
    QHBoxLayout *hbox = new QHBoxLayout;
    QLabel *label = new QLabel;
    label->setText(QString("LMAOOO"));
    hbox->addWidget(label);
    this->setLayout(hbox);

}

Node::Node(QWidget *parent): QWidget(parent){

}
Miner::Miner(QWidget *parent): QWidget(parent){

}
