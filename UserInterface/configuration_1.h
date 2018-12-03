#ifndef CONFIGURATION_1_H
#define CONFIGURATION_1_H

#include <QMainWindow>

namespace Ui {
class Configuration_1;
}

class Configuration_1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Configuration_1(QWidget *parent = nullptr);
    ~Configuration_1();

private:
    Ui::Configuration_1 *ui;
};

#endif // CONFIGURATION_1_H
