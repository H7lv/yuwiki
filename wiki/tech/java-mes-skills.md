---
title: Java MES 开发技能沉淀
tags: [java, spring, mes, skill]
created: 2026-06-29
updated: 2026-06-29
---

摘要：基于三年多 MES/ERP 系统开发经验沉淀的 Java 技术技能树，涵盖微服务架构、中间件、MES 领域知识。

## 微服务架构

### Spring Cloud Alibaba 全家桶
- Spring Boot / Spring Cloud 基础框架
- **Spring Cloud Gateway** — API 网关路由、鉴权、限流
- **Nacos** — 服务注册与配置中心
- **OpenFeign** — 声明式服务调用（30+ FeignClient 经验）
- **Sentinel** — 流量控制与熔断降级
- **Seata（AT 模式）** — 分布式事务处理
- **Spring Boot Admin** — 服务监控

### 基础框架
- **SpringBlade** — 二次开发经验，封装安全/日志/Swagger/MyBatis
- 自定义组合注解（如 `@MesCloudApplication`）

## 数据层

- **MyBatis-Plus** — ORM 框架深度使用（LambdaQueryWrapper、分页插件）
- **多租户** — MyBatis-Plus TenantLineInnerInterceptor 行级隔离
- **审计** — MetaObjectHandler 自动填充
- **MySQL 8.x** — 关系数据库设计与优化

## 中间件

- **Redis** — 缓存（Spring Data Redis、@Cacheable / @CacheEvict）
- **Kafka** — 消息队列（Spring Kafka）
- **RabbitMQ** — 消息队列（SMT 质检场景，Spring AMQP）
- **Apache Flink 1.18.1** — 流处理（从 Kafka 消费 → 写入 ES/Redis）
- **XXL-Job** — 分布式调度
- **Zipkin** — 分布式链路追踪

## MES 领域知识

### 核心业务模块
- **工单管理** — 工单执行、工序分配、流程跟踪（当前主要负责）
- **报工系统** — 完工汇报、人员/设备报工明细
- **流转码（条码）** — 生产流转跟踪，Barcode4J / ZXing
- **工艺路线** — 工序定义与路线配置
- **质量管理** — 不良代码、维修、返工流程
- **仓储管理** — 物料管理

### 业务表结构熟悉
工单执行主表、工单工序明细、完工汇报表、流转码表、流转过站记录、不良记录、工艺路线、物料表等。

## 开发工具

- **Maven** 多模块聚合（11 个模块）
- **Lombok** / **FastJSON2** / **Commons-Lang3**
- **EasyExcel** / **Apache POI** / **PDFBox**
- **Knife4j (Swagger)** — API 文档（320+ 接口注解）
- **Docker** / **Harbor** — 容器化部署
- 多环境配置（dev/test/prod）
- **涉密离线部署** — 军工项目现场部署经验：涉密内网环境、身份证换卡物理安全管控、离线依赖预装与故障排查

## 与 AI Agent 关联

这份技能中与 AI Agent 转型直接相关的部分：
- 微服务编排 → AI Agent 多工具编排
- Spring Cloud Gateway → AI Gateway / API 路由
- Flink 流处理 → Agent 流式数据处理
- 消息队列 → Agent 事件驱动架构
- 多租户隔离 → Agent 租户管理

详见 [[ai-agent-roadmap]]。

## 相关页面

- [[spring-mes-tech-stack]] — SpringMes 完整技术栈
- [[career-profile]] — 职业时间线
- [[ai-agent-roadmap]] — AI Agent 转型规划
