#include "configuration_1.h"
#include "ui_configuration_1.h"

Configuration_1::Configuration_1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Configuration_1)
{
    ui->setupUi(this);
}

Configuration_1::~Configuration_1()
{
    delete ui;
}
