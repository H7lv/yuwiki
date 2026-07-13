---
title: Java 面试自测清单
tags: [java, career, interview, checklist]
created: 2026-07-06
updated: 2026-07-06
---

摘要：Java 后端面试（3 年+经验，目标 13-15k，宁波）的完整自测清单。分六个梯队，每个知识点可自评：❌不会 / ⚠️能说两句 / ✅能讲清楚。

---

## 使用方式

在每个知识点后面标记：
- **❌** — 完全不会，需要从头学
- **⚠️** — 知道一些，但讲不清楚，需要复习
- **✅** — 能讲清楚原理和场景，面试不虚

**目标**：把所有 ❌ 和 ⚠️ 都变成 ✅

---

## 🔴 第一梯队：必问必会（占面试 60%）

### 一、JVM

- [ ] JVM 内存模型：堆 / 栈 / 方法区 / 程序计数器各存什么
- [ ] 堆的分代结构：Young / Old / Metaspace，为什么要分代
- [ ] 对象创建过程（类加载 → 内存分配 → 初始化）
- [ ] GC 基础：Minor GC / Major GC / Full GC 触发条件
- [ ] **CMS 垃圾收集器**：工作原理、优缺点、并发标记阶段
- [ ] **G1 垃圾收集器**：Region 划分、停顿预测模型、Mixed GC
- [ ] 对象什么时候进入老年代（年龄阈值 / 动态年龄 / 大对象）
- [ ] 类加载机制：双亲委派模型、如何打破、Tomcat 为什么打破
- [ ] OOM 排查：怎么 dump 堆、MAT 怎么看、常见 OOM 场景
- [ ] JVM 调优参数：-Xms/-Xmx、-XX:+UseG1GC、GC 日志怎么看
- [ ] 强引用 / 软引用 / 弱引用 / 虚引用 的区别和应用场景

### 二、并发编程

- [ ] **synchronized 原理**：锁升级过程（偏向锁 → 轻量级锁 → 重量级锁）
- [ ] synchronized 和 ReentrantLock 的区别
- [ ] **volatile 原理**：可见性、有序性（禁止指令重排）
- [ ] **AQS 框架原理**：CLH 队列、state 状态、独占/共享模式
- [ ] ReentrantLock：公平锁 vs 非公平锁、可重入
- [ ] **线程池 7 大参数**：corePoolSize / maxPoolSize / keepAliveTime / workQueue / threadFactory / RejectedExecutionHandler
- [ ] 拒绝策略：AbortPolicy / CallerRunsPolicy / DiscardPolicy / DiscardOldestPolicy
- [ ] 核心线程数怎么设 —— IO 密集型 vs CPU 密集型
- [ ] **ThreadLocal**：原理、内存泄漏问题、InheritableThreadLocal
- [ ] **CAS 原理**：ABA 问题、AtomicInteger 底层实现
- [ ] CountDownLatch / CyclicBarrier / Semaphore 的场景和区别

### 三、集合框架

- [ ] **HashMap 原理**：put / get 流程、数组+链表+红黑树
- [ ] **HashMap 扩容机制**：为什么容量是 2 的幂、加载因子为什么 0.75
- [ ] HashMap 线程安全问题（死循环问题 Java 7 / resize 竞态）
- [ ] **ConcurrentHashMap**：Java 7 分段锁 vs Java 8 synchronized+CAS
- [ ] ArrayList 底层结构、扩容机制（1.5 倍）
- [ ] ArrayList vs LinkedList 增删改查复杂度
- [ ] HashSet 底层原理（= HashMap）

---

## 🟡 第二梯队：实战经验整理（占面试 30%）

### 四、Spring 全家桶

- [ ] **IOC 原理**：Bean 生命周期（实例化 → 属性赋值 → 初始化 → 销毁）
- [ ] **循环依赖**：三级缓存怎么解决、为什么需要三级而不是两级
- [ ] **AOP 原理**：JDK 动态代理 vs CGLIB 区别
- [ ] @Transactional 失效场景（方法内部调用、private、异常被 catch）
- [ ] Spring Boot 自动配置原理（@EnableAutoConfiguration）
- [ ] Spring MVC 请求处理流程（DispatcherServlet）
- [ ] **Nacos**：注册中心原理（AP 协议 Distro）、配置中心（长轮询）
- [ ] **Gateway**：路由 / 断言 / 过滤器、自定义全局过滤器
- [ ] **Feign / OpenFeign**：声明式调用、负载均衡集成
- [ ] **Sentinel**：限流 / 熔断 / 降级、热点参数限流
- [ ] **分布式事务**：Seata AT 模式原理、TCC 模式适用场景
- [ ] **RocketMQ**：事务消息、顺序消息、重复消费处理、消息堆积

### 五、MySQL

- [ ] **索引结构**：B+Tree、聚簇索引 vs 非聚簇索引
- [ ] 最左前缀原则、索引下推、覆盖索引
- [ ] explain 怎么看：type / key / rows / Extra 各字段含义
- [ ] 慢 SQL 优化思路（索引 → 覆盖索引 → 分页优化）
- [ ] 大分页优化（游标分页 vs offset 分页）
- [ ] **事务隔离级别**：读未提交 / 读已提交 / 可重复读 / 串行化
- [ ] **MVCC 原理**：undo log 版本链 + ReadView
- [ ] 当前读 vs 快照读
- [ ] **间隙锁 / Next-Key 锁**：解决幻读
- [ ] 分库分表：ShardingSphere 原理、分片策略

### 六、Redis

- [ ] 5 种数据结构及场景：String / Hash / List / Set / ZSet
- [ ] **缓存穿透**：布隆过滤器
- [ ] **缓存击穿**：互斥锁 / 逻辑过期
- [ ] **缓存雪崩**：过期时间加随机值 / 多级缓存
- [ ] 缓存和数据库一致性问题（先删缓存？先更新 DB？最终方案）
- [ ] **Redis 分布式锁**：setnx + expire + Lua、Redisson
- [ ] Redis 持久化：RDB 全量快照 vs AOF 增量日志
- [ ] Redis 集群模式：主从 / 哨兵 / Cluster

---

## 🟢 第三梯队：刷刷就能答（占面试 10%）

### 七、计算机网络

- [ ] TCP 三次握手 / 四次挥手
- [ ] TCP 和 UDP 区别
- [ ] HTTP / HTTPS 区别，SSL/TLS 握手过程
- [ ] 浏览器输入 URL 到页面展示全过程
- [ ] HTTP 状态码：200 / 301 / 302 / 401 / 403 / 404 / 500 / 502 / 503

### 八、Linux 基础

- [ ] 常用命令：top / ps / jps / jstack / jstat / jmap / grep / awk
- [ ] 怎么查日志（tail -f、grep 关键字、less 翻页）
- [ ] 线上 CPU 100% 怎么排查（top → jstack → 分析线程栈）
- [ ] 线上 OOM 怎么排查

### 九、算法（LeetCode Hot 100）

- [ ] 两数之和
- [ ] 反转链表
- [ ]  LRU 缓存（面试高频！）
- [ ] 有效的括号
- [ ] 合并两个有序链表
- [ ] 二叉树遍历（前/中/后序）
- [ ] 最长回文子串
- [ ] 快排 / 归并排序（手写）
- [ ] 二分查找
- [ ] 字符串相加/相乘
- [ ] Top K 问题（堆 / 快排分区）

---

## 🔵 第四梯队：项目亮点包装（面试决定分）

### 十、3 分钟讲清楚你的 4 个项目（STAR 法）

#### 项目 1：MES 扫码上料系统（军工）

- [ ] S：军工客户，扫码上料，质量和追溯要求极高
- [ ] T：涉密内网，完全离线，依赖包预装，无互联网排错
- [ ] A：驻场 1 个月，离线环境部署调试，身份证换卡进入
- [ ] R：系统上线验收，通过军工质量审核
- [ ] **核心价值**：24 岁独立驻场搞定军工项目，态度和能力都硬

#### 项目 2：MES 飞达制造 SpringMes（当前）

- [ ] S：Spring Cloud Alibaba 微服务架构 MES
- [ ] T：工单管理模块复杂业务，多工序流转
- [ ] A：独立负责，Spring Cloud 组件全套使用
- [ ] R：系统开发推进中
- [ ] **核心价值**：展示你当前的技术水平

#### 项目 3：ERP 系统

- [ ] S：电子行业 ERP，业务模块庞大
- [ ] T：从 C++ 转 Java 后第一个大项目
- [ ] A：负责销售模块 + 财务总账模块
- [ ] R：从 Java 零基础到独立搞一个模块
- [ ] **核心价值**：学习能力强，适应力好

#### 项目 4：MES 数据上报系统

- [ ] 简要概括即可（补充项目丰富度）

### 十一、让面试官记住你的差异点

- [ ] "我从 C++ Qt 转 Java，边学边做了 4 个企业级系统，学习能力我很有信心"
- [ ] "我独立驻场过一个军工项目，涉密内网离线部署，扛得住压力"
- [ ] "我现在业余时间在学 AI Agent，Python / LangChain 都有涉及"

---

## 🟣 第五梯队：薪资谈判准备

- [ ] 问清楚：月 base 多少，一年几个月薪，有没有绩效奖金
- [ ] 你的底线 12k，目标 14k，拼一把 15k
- [ ] 反问：公积金比例？一年调薪几次？涨薪幅度？

---

## 📊 自测总评

```
🔴 JVM 并发 集合      ❌___ / ⚠️___ / ✅___  （共约 30 项）
🟡 Spring MySQL Redis ❌___ / ⚠️___ / ✅___  （共约 35 项）
🟢 网络 Linux 算法     ❌___ / ⚠️___ / ✅___  （共约 20 项）
🔵 项目包装           ❌___ / ⚠️___ / ✅___  （共约 15 项）
```

## 📅 建议复习顺序

```
第 1 周：JVM + 集合          → 把第一梯队的硬骨头啃掉
第 2 周：并发                  → 并发是 3年+ 面试必问重点
第 3 周：Spring 全家桶整理      → 你最熟，整理成面试稿就行
第 4 周：MySQL + Redis         → 穿插复习
第 5 周：项目亮点包装           → 写 STAR 稿，对着镜子练
第 6 周：刷题 20 道 + 投简历
```

---

## 关联页面

- [[career-profile]] — 你的职业经历
- [[ai-agent-roadmap]] — AI Agent 学习路线
- [[ai-agent-developer-tech-stack]] — AI 岗位技术栈
