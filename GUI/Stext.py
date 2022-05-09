/********************************************************************************
** Form generated from reading UI file 'Stext.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef STEXT_H
#define STEXT_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen;
    QAction *actionQuit;
    QAction *actionabout_the_program;
    QAction *actionAbout_Stext;
    QAction *actionAbout_image_editor;
    QAction *actionSettings;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QPushButton *pushButton;
    QPlainTextEdit *plainTextEdit;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuHelp;
    QMenu *menuInfo;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(270, 306);
        QFont font;
        font.setPointSize(8);
        MainWindow->setFont(font);
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QString::fromUtf8("actionOpen"));
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName(QString::fromUtf8("actionQuit"));
        actionabout_the_program = new QAction(MainWindow);
        actionabout_the_program->setObjectName(QString::fromUtf8("actionabout_the_program"));
        actionAbout_Stext = new QAction(MainWindow);
        actionAbout_Stext->setObjectName(QString::fromUtf8("actionAbout_Stext"));
        actionAbout_image_editor = new QAction(MainWindow);
        actionAbout_image_editor->setObjectName(QString::fromUtf8("actionAbout_image_editor"));
        actionSettings = new QAction(MainWindow);
        actionSettings->setObjectName(QString::fromUtf8("actionSettings"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setMouseTracking(false);

        verticalLayout->addWidget(pushButton);

        plainTextEdit = new QPlainTextEdit(centralwidget);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setMinimumSize(QSize(250, 220));
        QFont font1;
        font1.setPointSize(10);
        plainTextEdit->setFont(font1);

        verticalLayout->addWidget(plainTextEdit);


        verticalLayout_2->addLayout(verticalLayout);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 270, 19));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        QIcon icon(QIcon::fromTheme(QString::fromUtf8("oxygen")));
        menuFile->setIcon(icon);
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        menuInfo = new QMenu(menuHelp);
        menuInfo->setObjectName(QString::fromUtf8("menuInfo"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuHelp->menuAction());
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionSettings);
        menuFile->addSeparator();
        menuFile->addAction(actionQuit);
        menuHelp->addAction(menuInfo->menuAction());
        menuHelp->addSeparator();
        menuHelp->addAction(actionabout_the_program);
        menuInfo->addAction(actionAbout_Stext);
        menuInfo->addAction(actionAbout_image_editor);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Stext", nullptr));
#if QT_CONFIG(accessibility)
        MainWindow->setAccessibleDescription(QCoreApplication::translate("MainWindow", "When you click on the button, a screenshot appears", nullptr));
#endif // QT_CONFIG(accessibility)
        actionOpen->setText(QCoreApplication::translate("MainWindow", "Open", nullptr));
        actionQuit->setText(QCoreApplication::translate("MainWindow", "Quit", nullptr));
        actionabout_the_program->setText(QCoreApplication::translate("MainWindow", "About the program", nullptr));
        actionAbout_Stext->setText(QCoreApplication::translate("MainWindow", "About Stext", nullptr));
        actionAbout_image_editor->setText(QCoreApplication::translate("MainWindow", "About image editor", nullptr));
        actionSettings->setText(QCoreApplication::translate("MainWindow", "Settings", nullptr));
#if QT_CONFIG(accessibility)
        pushButton->setAccessibleDescription(QCoreApplication::translate("MainWindow", "When you click on the button, a screenshot appears", "When you click on the button, a screenshot appears"));
#endif // QT_CONFIG(accessibility)
        pushButton->setText(QCoreApplication::translate("MainWindow", "Screen shot", nullptr));
        plainTextEdit->setPlainText(QString());
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("MainWindow", "Help", nullptr));
        menuInfo->setTitle(QCoreApplication::translate("MainWindow", "Info", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // STEXT_H
