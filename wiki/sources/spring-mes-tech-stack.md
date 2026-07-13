---
title: SpringMes MES 技术栈详情
tags: [java, spring, mes, reference]
created: 2026-06-29
updated: 2026-06-29
source: 用户口述+提供的技术栈清单
type: source-note
---

摘要：SpringMes 项目完整技术栈记录，基于 Spring Cloud Alibaba 微服务架构的制造执行系统（MES）。三个 MES 系统共用此技术栈。

## 核心内容

SpringMes 是一套基于 Spring Cloud Alibaba 微服务架构的制造执行系统，包含 11 个微服务模块，覆盖生产制造全流程（工单/报工/流转码/追溯/质检/仓储）。

## 技术栈详情

### 核心框架

- **Spring Boot 2.7.1** — 基础框架
- **Spring Cloud 2021.0.3** — 微服务治理
- **Spring Cloud Alibaba 2021.0.1.0** — 阿里云微服务套件
- **SpringBlade 3.5.0** — 基础开发框架（封装安全/日志/Swagger/MyBatis）
- **Spring Cloud Gateway** — API 网关
- **Spring Cloud OpenFeign** — 声明式服务调用（30+ FeignClient）
- **MyBatis-Plus 3.5.2** — ORM 框架

### 中间件与基础设施

- **Nacos 2.1.0** — 服务注册与配置中心
- **Seata 1.6.1** — 分布式事务（AT 模式）
- **Sentinel** — 流量控制/熔断降级
- **MySQL 8.x** — 关系数据库
- **Redis** — 缓存（Spring Data Redis / Jedis）
- **Kafka** — 消息队列
- **RabbitMQ** — 消息队列（SMT 质检）
- **Apache Flink 1.18.1** — 流处理（从 Kafka 读取 → 写入 ES/Redis）
- **Zipkin** — 分布式链路追踪
- **XXL-Job** — 分布式调度
- **Spring Boot Admin 2.7.1** — 服务监控

### 服务模块（11 个）

| 模块 | 说明 |
|---|---|
| mes-gateway | API 网关（路由、鉴权、限流） |
| mes-auth | 认证授权 |
| mes-system | 系统管理（菜单/角色/字典） |
| mes-user | 用户服务 |
| **mes-manufact** | **生产制造核心（报工/流转码/工单/看板）** |
| mes-storehouse | 仓储管理 |
| mes-quality | 质量管理（不良/维修/返工） |
| mes-traceability | 追溯服务（WebSocket 看板推送） |
| mes-filestorage | 文件存储（FastDFS + MinIO） |
| mes-flink-job | Flink 流处理作业 |

### 认证与安全

- JWT（JJWT 0.11.2）Token 鉴权
- SpringBlade Secure 认证/授权封装
- Hibernate Validator 参数校验
- easy-captcha 验证码

### 文件与导出

- Alibaba EasyExcel 2.2.6 — Excel 导入导出
- Apache POI — 传统 Excel 操作
- Apache PDFBox 3.0.2 — PDF 处理
- Barcode4J / ZXing — 条码/二维码生成
- FastDFS — 分布式文件存储
- MinIO — S3 兼容对象存储

### 部署

- Docker（8 模块独立 Dockerfile）
- Harbor 镜像仓库
- 三套环境：dev（192.168.9.88）/ test（192.168.9.244）/ prod（172.21.9.144）

### 核心业务表

工单执行主表、工单工序明细、完工汇报（报工单）、报工人员/设备明细、流转码、流转过站/不良记录、工艺路线、物料、车间、不良代码等。

## 要点提炼

- 搭建时**参考了前领导的项目架构**，在此基础上自己搭建
- 11 个微服务模块，以 `mes-manufact` 为生产核心
- 消息队列双方案：Kafka（主）+ RabbitMQ（SMT 质检）
- Flink 做流处理，从 Kafka 消费写入 ES/Redis
- 多租户使用 MyBatis-Plus 行级隔离
- 30+ FeignClient，统一在 `mes-service-api` 模块定义

## 个人思考

这是当前主力项目，技术栈覆盖面很广——从微服务治理到流处理到文件存储都有了。工单管理是核心业务模块之一。

与 [[ai-agent-roadmap]] 对比来看，当前技术栈中 Seata/Sentinel/Nacos/Flink 这些分布式中间件经验，可以转化为 AI Agent 中的工具调用、多服务编排等能力的理解。

## 影响的知识页面

此资料更新了以下页面：
- [[career-profile]] — 完善项目时间线和角色
- [[java-mes-skills]] — 技术沉淀页面
