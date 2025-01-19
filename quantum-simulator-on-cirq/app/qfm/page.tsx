'use client'
import { useState } from 'react';
import { Layout, Menu } from 'antd';
import GeneralInfo from '@/components/GeneralInfo/page';
import SimpleExample from '@/components/SimpleExample/page';
import MeasureOnceQFA from '@/components/MeasureOnceQFA/page';
import MeasureManyQFA from '@/components/MeasureManyQFA/page';
import OneWayQFA from '@/components/OneWayQFA/page';
import TwoWayQFA from '@/components/TwoWayQFA/page';
import QFARestart from '@/components/QFARestart/page';
import QFAControlLanguage from '@/components/QFAControlLanguage/page';

const { Content, Sider } = Layout;

const QFMPage = () => {
    const [selectedTab, setSelectedTab] = useState('general-info');

    const renderContent = () => {
        switch (selectedTab) {
            case 'general-info':
                return <GeneralInfo />;
            case 'simple-example':
                return <SimpleExample />;
            case 'measure-once':
                return <MeasureOnceQFA />;
            case 'measure-many':
                return <MeasureManyQFA />;
            case 'one-way-qfa':
                return <OneWayQFA />;
            case 'two-way-qfa':
                return <TwoWayQFA />;
            case 'qfa-restart':
                return <QFARestart />;
            case 'qfa-control-language':
                return <QFAControlLanguage />;
            default:
                return <GeneralInfo />;
        }
    };

    return (
        <Layout style={{ minHeight: '100vh' }}>
            <Sider width={200} theme="light">
                <Menu
                    mode="inline"
                    defaultSelectedKeys={['general-info']}
                    style={{ height: '100%', borderRight: 0 }}
                    onSelect={({ key }) => setSelectedTab(key as string)}
                >
                    <Menu.Item key="general-info">General Info</Menu.Item>
                    <Menu.Item key="simple-example">Simple Example</Menu.Item>
                    <Menu.SubMenu key="types" title="Types of QFMs">
                        <Menu.Item key="measure-once">Measure-Once QFA</Menu.Item>
                        <Menu.Item key="measure-many">Measure-Many QFA</Menu.Item>
                        <Menu.Item key="one-way-qfa">One-Way QFA</Menu.Item>
                        <Menu.Item key="two-way-qfa">Two-Way QFA</Menu.Item>
                        <Menu.Item key="qfa-restart">QFA with Restart</Menu.Item>
                        <Menu.Item key="qfa-control-language">QFA with Control Language</Menu.Item>
                    </Menu.SubMenu>
                </Menu>
            </Sider>
            <Layout>
                <Content style={{ padding: '24px' }}>
                    {renderContent()}
                </Content>
            </Layout>
        </Layout>
    );
};

export default QFMPage;