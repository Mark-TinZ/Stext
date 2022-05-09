/********************************************************************************
** Form generated from reading UI file 'Stext_Settings.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef STEXT_SETTINGS_H
#define STEXT_SETTINGS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_8;
    QVBoxLayout *verticalLayout_7;
    QHBoxLayout *horizontalLayout_4;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_5;
    QVBoxLayout *verticalLayout_4;
    QRadioButton *L_theam;
    QRadioButton *D_theam;
    QRadioButton *O_theam;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_2;
    QLabel *Red_lable;
    QSpinBox *R_spin;
    QVBoxLayout *verticalLayout;
    QLabel *Green_lable;
    QSpinBox *G_spin;
    QVBoxLayout *verticalLayout_3;
    QLabel *Blue_lable;
    QSpinBox *B_spin;
    QVBoxLayout *verticalLayout_6;
    QHBoxLayout *horizontalLayout_2;
    QLabel *Text_size;
    QSpinBox *Size_spin;
    QHBoxLayout *horizontalLayout_3;
    QLabel *App_lang;
    QComboBox *Lang_combo;
    QSpacerItem *verticalSpacer;
    QCheckBox *Save_image;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *Close_settings;
    QPushButton *Reset_settings;
    QSpacerItem *horizontalSpacer;
    QPushButton *Apply_settings;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(481, 250);
        MainWindow->setMinimumSize(QSize(481, 250));
        MainWindow->setMaximumSize(QSize(481, 250));
        MainWindow->setIconSize(QSize(24, 24));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_8 = new QVBoxLayout(centralwidget);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_5 = new QVBoxLayout(groupBox);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        L_theam = new QRadioButton(groupBox);
        L_theam->setObjectName(QString::fromUtf8("L_theam"));
        L_theam->setChecked(true);

        verticalLayout_4->addWidget(L_theam);

        D_theam = new QRadioButton(groupBox);
        D_theam->setObjectName(QString::fromUtf8("D_theam"));

        verticalLayout_4->addWidget(D_theam);

        O_theam = new QRadioButton(groupBox);
        O_theam->setObjectName(QString::fromUtf8("O_theam"));

        verticalLayout_4->addWidget(O_theam);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        Red_lable = new QLabel(groupBox);
        Red_lable->setObjectName(QString::fromUtf8("Red_lable"));
        Red_lable->setTextFormat(Qt::AutoText);
        Red_lable->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(Red_lable);

        R_spin = new QSpinBox(groupBox);
        R_spin->setObjectName(QString::fromUtf8("R_spin"));
        R_spin->setEnabled(false);
        R_spin->setAlignment(Qt::AlignCenter);
        R_spin->setButtonSymbols(QAbstractSpinBox::NoButtons);
        R_spin->setKeyboardTracking(true);
        R_spin->setMaximum(255);

        verticalLayout_2->addWidget(R_spin);


        horizontalLayout->addLayout(verticalLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        Green_lable = new QLabel(groupBox);
        Green_lable->setObjectName(QString::fromUtf8("Green_lable"));
        Green_lable->setTextFormat(Qt::AutoText);
        Green_lable->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(Green_lable);

        G_spin = new QSpinBox(groupBox);
        G_spin->setObjectName(QString::fromUtf8("G_spin"));
        G_spin->setEnabled(false);
        G_spin->setAlignment(Qt::AlignCenter);
        G_spin->setButtonSymbols(QAbstractSpinBox::NoButtons);
        G_spin->setKeyboardTracking(true);
        G_spin->setMaximum(255);

        verticalLayout->addWidget(G_spin);


        horizontalLayout->addLayout(verticalLayout);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        Blue_lable = new QLabel(groupBox);
        Blue_lable->setObjectName(QString::fromUtf8("Blue_lable"));
        Blue_lable->setTextFormat(Qt::AutoText);
        Blue_lable->setAlignment(Qt::AlignCenter);

        verticalLayout_3->addWidget(Blue_lable);

        B_spin = new QSpinBox(groupBox);
        B_spin->setObjectName(QString::fromUtf8("B_spin"));
        B_spin->setEnabled(false);
        B_spin->setAlignment(Qt::AlignCenter);
        B_spin->setButtonSymbols(QAbstractSpinBox::NoButtons);
        B_spin->setKeyboardTracking(true);
        B_spin->setMaximum(255);

        verticalLayout_3->addWidget(B_spin);


        horizontalLayout->addLayout(verticalLayout_3);


        verticalLayout_4->addLayout(horizontalLayout);


        verticalLayout_5->addLayout(verticalLayout_4);


        horizontalLayout_4->addWidget(groupBox);

        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        Text_size = new QLabel(centralwidget);
        Text_size->setObjectName(QString::fromUtf8("Text_size"));

        horizontalLayout_2->addWidget(Text_size);

        Size_spin = new QSpinBox(centralwidget);
        Size_spin->setObjectName(QString::fromUtf8("Size_spin"));
        Size_spin->setMinimumSize(QSize(70, 0));
        Size_spin->setMinimum(8);
        Size_spin->setMaximum(100);

        horizontalLayout_2->addWidget(Size_spin);


        verticalLayout_6->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        App_lang = new QLabel(centralwidget);
        App_lang->setObjectName(QString::fromUtf8("App_lang"));

        horizontalLayout_3->addWidget(App_lang);

        Lang_combo = new QComboBox(centralwidget);
        Lang_combo->addItem(QString());
        Lang_combo->addItem(QString());
        Lang_combo->setObjectName(QString::fromUtf8("Lang_combo"));

        horizontalLayout_3->addWidget(Lang_combo);


        verticalLayout_6->addLayout(horizontalLayout_3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_6->addItem(verticalSpacer);

        Save_image = new QCheckBox(centralwidget);
        Save_image->setObjectName(QString::fromUtf8("Save_image"));

        verticalLayout_6->addWidget(Save_image);


        horizontalLayout_4->addLayout(verticalLayout_6);


        verticalLayout_7->addLayout(horizontalLayout_4);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        Close_settings = new QPushButton(centralwidget);
        Close_settings->setObjectName(QString::fromUtf8("Close_settings"));

        horizontalLayout_5->addWidget(Close_settings);

        Reset_settings = new QPushButton(centralwidget);
        Reset_settings->setObjectName(QString::fromUtf8("Reset_settings"));

        horizontalLayout_5->addWidget(Reset_settings);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer);

        Apply_settings = new QPushButton(centralwidget);
        Apply_settings->setObjectName(QString::fromUtf8("Apply_settings"));

        horizontalLayout_5->addWidget(Apply_settings);


        verticalLayout_7->addLayout(horizontalLayout_5);


        verticalLayout_8->addLayout(verticalLayout_7);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);
        QObject::connect(O_theam, SIGNAL(clicked(bool)), R_spin, SLOT(setEnabled(bool)));
        QObject::connect(O_theam, SIGNAL(clicked(bool)), B_spin, SLOT(setEnabled(bool)));
        QObject::connect(O_theam, SIGNAL(clicked(bool)), G_spin, SLOT(setEnabled(bool)));
        QObject::connect(L_theam, SIGNAL(clicked(bool)), B_spin, SLOT(setDisabled(bool)));
        QObject::connect(D_theam, SIGNAL(clicked(bool)), G_spin, SLOT(setDisabled(bool)));
        QObject::connect(D_theam, SIGNAL(clicked(bool)), R_spin, SLOT(setDisabled(bool)));
        QObject::connect(D_theam, SIGNAL(clicked(bool)), B_spin, SLOT(setDisabled(bool)));
        QObject::connect(L_theam, SIGNAL(clicked(bool)), G_spin, SLOT(setDisabled(bool)));
        QObject::connect(L_theam, SIGNAL(clicked(bool)), R_spin, SLOT(setDisabled(bool)));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Staxt - Settings", nullptr));
        groupBox->setTitle(QCoreApplication::translate("MainWindow", "Themes", nullptr));
        L_theam->setText(QCoreApplication::translate("MainWindow", "Light theme", nullptr));
        D_theam->setText(QCoreApplication::translate("MainWindow", "Dark theme", nullptr));
        O_theam->setText(QCoreApplication::translate("MainWindow", "Own theme", nullptr));
        Red_lable->setText(QCoreApplication::translate("MainWindow", "R", nullptr));
        R_spin->setSuffix(QCoreApplication::translate("MainWindow", " - 255", nullptr));
        Green_lable->setText(QCoreApplication::translate("MainWindow", "G", nullptr));
        G_spin->setSuffix(QCoreApplication::translate("MainWindow", " - 255", nullptr));
        Blue_lable->setText(QCoreApplication::translate("MainWindow", "B", nullptr));
        B_spin->setSuffix(QCoreApplication::translate("MainWindow", " - 255", nullptr));
        Text_size->setText(QCoreApplication::translate("MainWindow", "Text size", nullptr));
        Size_spin->setSuffix(QString());
        App_lang->setText(QCoreApplication::translate("MainWindow", "App language", nullptr));
        Lang_combo->setItemText(0, QCoreApplication::translate("MainWindow", "English", nullptr));
        Lang_combo->setItemText(1, QCoreApplication::translate("MainWindow", "Russian", nullptr));

        Save_image->setText(QCoreApplication::translate("MainWindow", "Save images", nullptr));
        Close_settings->setText(QCoreApplication::translate("MainWindow", "Close", nullptr));
        Reset_settings->setText(QCoreApplication::translate("MainWindow", "Reset", nullptr));
        Apply_settings->setText(QCoreApplication::translate("MainWindow", "Apply", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // STEXT_SETTINGS_H
