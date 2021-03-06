# pylint: skip-file

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.btnOrder = QtWidgets.QToolButton(self.centralwidget)
        self.btnOrder.setObjectName("btnOrder")
        self.horizontalLayout_4.addWidget(self.btnOrder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setEnabled(False)
        self.btnExport.setObjectName("btnExport")
        self.gridLayout_3.addWidget(self.btnExport, 0, 3, 1, 1)
        self.btnInstall = QtWidgets.QPushButton(self.centralwidget)
        self.btnInstall.setObjectName("btnInstall")
        self.gridLayout_3.addWidget(self.btnInstall, 0, 0, 1, 1)
        self.btnRemerge = QtWidgets.QToolButton(self.centralwidget)
        self.btnRemerge.setStyleSheet("padding: 3px 10px 2px;")
        self.btnRemerge.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.btnRemerge.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnRemerge.setArrowType(QtCore.Qt.NoArrow)
        self.btnRemerge.setObjectName("btnRemerge")
        self.gridLayout_3.addWidget(self.btnRemerge, 0, 1, 1, 1)
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setEnabled(False)
        self.btnChange.setObjectName("btnChange")
        self.gridLayout_3.addWidget(self.btnChange, 0, 2, 1, 1)
        self.btnBackup = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackup.setObjectName("btnBackup")
        self.gridLayout_3.addWidget(self.btnBackup, 1, 0, 1, 1)
        self.btnRestore = QtWidgets.QPushButton(self.centralwidget)
        self.btnRestore.setObjectName("btnRestore")
        self.gridLayout_3.addWidget(self.btnRestore, 1, 1, 1, 1)
        self.btnRemoveAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoveAll.setObjectName("btnRemoveAll")
        self.gridLayout_3.addWidget(self.btnRemoveAll, 1, 2, 1, 1)
        self.btnCemu = QtWidgets.QPushButton(self.centralwidget)
        self.btnCemu.setObjectName("btnCemu")
        self.gridLayout_3.addWidget(self.btnCemu, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(276, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblImage = QtWidgets.QLabel(self.groupBox)
        self.lblImage.setText("")
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.verticalLayout.addWidget(self.lblImage)
        self.lblModInfo = QtWidgets.QLabel(self.groupBox)
        self.lblModInfo.setObjectName("lblModInfo")
        self.verticalLayout.addWidget(self.lblModInfo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnUninstall = QtWidgets.QPushButton(self.groupBox)
        self.btnUninstall.setEnabled(False)
        self.btnUninstall.setObjectName("btnUninstall")
        self.horizontalLayout_2.addWidget(self.btnUninstall)
        self.btnDisableMod = QtWidgets.QPushButton(self.groupBox)
        self.btnDisableMod.setEnabled(False)
        self.btnDisableMod.setObjectName("btnDisableMod")
        self.horizontalLayout_2.addWidget(self.btnDisableMod)
        self.btnEnableMod = QtWidgets.QPushButton(self.groupBox)
        self.btnEnableMod.setEnabled(False)
        self.btnEnableMod.setVisible(False)
        self.btnEnableMod.setObjectName("btnEnableMod")
        self.horizontalLayout_2.addWidget(self.btnEnableMod)
        self.btnExplore = QtWidgets.QPushButton(self.groupBox)
        self.btnExplore.setEnabled(False)
        self.btnExplore.setObjectName("btnExplore")
        self.horizontalLayout_2.addWidget(self.btnExplore)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(2, 6)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("margin-right: 8px;")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInstallFolder = QtWidgets.QAction(MainWindow)
        self.actionInstallFolder.setIconVisibleInMenu(False)
        self.actionInstallFolder.setObjectName("actionInstallFolder")
        self.actionInstallMultiple = QtWidgets.QAction(MainWindow)
        self.actionInstallMultiple.setIconVisibleInMenu(False)
        self.actionInstallMultiple.setObjectName("actionInstallMultiple")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "BCML: BotW Cemu Mod Loader", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Installed Mods", None, -1))
        self.btnOrder.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Toggle the order in which mods are displayed.\nDefault lists mods from highest priority to lowest priority, but can be reversed.", None, -1))
        self.btnOrder.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.listWidget.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Drag and drop to change mod load order. Mods at the top of the list override mods at the bottom.", None, -1))
        self.btnInstall.setText(QtWidgets.QApplication.translate("MainWindow", "Install...", None, -1))
        self.btnRemerge.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Perform all merges again", None, -1))
        self.btnRemerge.setText(QtWidgets.QApplication.translate("MainWindow", "Remerge", None, -1))
        self.btnChange.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Apply changes to load order", None, -1))
        self.btnChange.setText(QtWidgets.QApplication.translate("MainWindow", " Apply Sort", None, -1))
        self.btnExport.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Export installed mods as a single mod", None, -1))
        self.btnExport.setText(QtWidgets.QApplication.translate("MainWindow", "Export...", None, -1))
        self.btnBackup.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates a backup of all currently installed mods", None, -1))
        self.btnBackup.setText(QtWidgets.QApplication.translate("MainWindow", "Backup Mods", None, -1))
        self.btnRestore.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Restores a mod configuration backup", None, -1))
        self.btnRestore.setText(QtWidgets.QApplication.translate("MainWindow", "Restore...", None, -1))
        self.btnRemoveAll.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Uninstalls all mods and clears BCML's master pack", None, -1))
        self.btnRemoveAll.setText(QtWidgets.QApplication.translate("MainWindow", "Uninstall All", None, -1))
        self.btnCemu.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Open Cemu and run Breath of the Wild", None, -1))
        self.btnCemu.setText(QtWidgets.QApplication.translate("MainWindow", "Launch Game", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Mod Info", None, -1))
        self.lblModInfo.setText(QtWidgets.QApplication.translate("MainWindow", "No mod selected", None, -1))
        self.btnUninstall.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Uninstall the selected mod", None, -1))
        self.btnUninstall.setText(QtWidgets.QApplication.translate("MainWindow", "Uninstall", None, -1))
        self.btnDisableMod.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Disable the selected mod", None, -1))
        self.btnDisableMod.setText(QtWidgets.QApplication.translate("MainWindow", "Disable", None, -1))
        self.btnEnableMod.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Enable the selected mod", None, -1))
        self.btnEnableMod.setText(QtWidgets.QApplication.translate("MainWindow", "Enable", None, -1))
        self.btnExplore.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Open the selected mod in your default file manager", None, -1))
        self.btnExplore.setText(QtWidgets.QApplication.translate("MainWindow", "Explore...", None, -1))
        self.actionInstallFolder.setText(QtWidgets.QApplication.translate("MainWindow", "Install from Folder", None, -1))
        self.actionInstallMultiple.setText(QtWidgets.QApplication.translate("MainWindow", "Install Multiple", None, -1))

