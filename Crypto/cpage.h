#ifndef CPAGE_H
#define CPAGE_H
#include <QWidget>


class Miner : public QWidget
{
public:
    Miner(QWidget *parent = 0);
};

class Wallet : public QWidget
{
public:
    Wallet(QWidget *parent = 0);
};

class Node : public QWidget
{
public:
    Node(QWidget *parent = 0);
};

#endif // CPAGE_H
