//package com.vision.ultron.config;
//
//import org.springframework.ai.embedding.EmbeddingModel;
//import org.springframework.ai.vectorstore.VectorStore;
//import org.springframework.ai.vectorstore.mongodb.atlas.MongoDBAtlasVectorStore;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.data.mongodb.core.MongoTemplate;
//
//@Configuration
//public class VectorStoreConfig {
//
//    @Bean
//    public MongoDBAtlasVectorStore vectorStore(MongoTemplate mongoTemplate, EmbeddingModel embeddingModel) {
//        return MongoDBAtlasVectorStore.builder(mongoTemplate, embeddingModel)
//                .pathName("your_database_name")  // Replace with your database name
//                .collectionName("your_collection_name")  // Replace with your collection name
//                .vectorIndexName("your_embedding_field")  // Replace with your embedding field
//                .build();
//    }
//}
